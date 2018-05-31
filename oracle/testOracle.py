#!/usr/bin/python
# -*- encoding: utf-8 -*-
import json
import os
import time
# 或者os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AL32UTF8'
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

import cx_Oracle
conn = cx_Oracle.connect('TMS2018/jsd1234@localhost:1521/orcl')

from datetime import datetime
from elasticsearch import Elasticsearch

# es = Elasticsearch([{'host': '47.97.208.67', 'port': '9200'}])
es = Elasticsearch(
    [
        'http://SFZ:123456@@47.97.208.67:9200/',
    ],
    verify_certs=True
)
print('--------------------------', es)

# select table
cursor = conn.cursor()
cursor.execute('SELECT TABLE_NAME FROM USER_TABLES')

exceptColumnName = ('PROVINCEID',)

i = 0
for tn in cursor:
    if (''.join(tn) == 'DEALER') | (''.join(tn) == 'PROVINCE'):
        # if (''.join(tn) == 'DEALER'):
        cursorColumn = conn.cursor()
        sqlColumn = ''' SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME = \'%s\' ''' % (
            tn)

        # i = i + 1

        # indexName = ''' \'TMS_%s \' ''' % (tn)
        # es.indices.create(index= indexName, ignore)

        # if i == 1:
        # 查询到数据库表的列名
        cursorColumn.execute(sqlColumn)
        columnTuple = ()
        for column in cursorColumn:
            columnTuple = columnTuple + column

        cursorRow = conn.cursor()
        sqlRow = ''' SELECT %s FROM %s ''' % (
            ','.join(columnTuple), ''.join(tn))

        # 查询到数据库表数据
        cursorRow.execute(sqlRow)

        dicRow = {}
        for row in cursorRow:
            # 处理 row
            # print(row)
            # 组织JSON值
            for index in range(len(row)):
                if columnTuple[index] in exceptColumnName:
                    dictKey = columnTuple[index]
                    dicRow['PROVINCE'] = {'PROVINCEID': row[index]}
                else:
                    dictKey = ('.'.join(tn)).upper() + columnTuple[index]

                if row[index] is None:
                    dicRow[dictKey] = ''
                elif isinstance(row[index], datetime):
                    dicRow[dictKey] = row[index].strftime('%Y-%m-%dT%H:%M:%S')
                elif isinstance(row[index], str):
                    dicRow[dictKey] = (row[index]).replace(
                        '"', ' ').replace("'", ' ')
                elif isinstance(row[index], cx_Oracle.LOB):
                    dicRow[dictKey] = str(row[index]).replace(
                        '"', ' ').replace("'", ' ')
                else:
                    dicRow[dictKey] = row[index]

            # 转为字符串
            print(type(str(dicRow)), '.....', str(dicRow).replace('\'', '\"'))

            es.index(index=('TMS_' + ''.join(tn)).lower(), doc_type=('TMS_' + ''.join(tn) + "_TYPE").lower(),
                     body=str(dicRow).replace('\'', '\"'))
            #  body=str(dicRow).replace('\'', '\"'), timestamp=(datetime.now()).strftime('%Y-%m-%dT%H:%M:%S'))

            # time.sleep(1)

cursor.close()
conn.close()

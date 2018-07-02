#!/usr/bin/python3.4
#coding=utf-8

import json
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch(
    [
        'http://192.168.101.109:9200',
    ],
    verify_certs=True
)

import cx_Oracle
conn = cx_Oracle.connect('TMSTEST2018/jsd1234@210.12.100.229:1521/jsd')

# 查询GPSSYNCADDRESS中存在的最大ID，实现增量同步
isESUp = es.ping()

if not isESUp:
    print('ES 没有启动起来，不能往下执行')
    os._exit(0)

isExist = es.indices.exists_type(
    index='tms_gps-sync-address',
    doc_type='tms_gps-sync-address_type',
)

MAXGPSADDRESSID = 0

if isExist:
    queryParams = es.search(
        index='tms_gps-sync-address',
        doc_type='tms_gps-sync-address_type',
        size=1,
        body={
            "sort": [
                {
                "GPSSYNCADDRESS_ID": {
                    "order": "desc"
                }
                }
            ]
        }
    )

    MAXGPSADDRESSID = queryParams['hits']['hits'][0]['_source']['GPSSYNCADDRESS_ID']
else:
    print('还没有创建Index，需要先创建')

DBTABLENAME = ('GPSSYNCADDRESS',)

# 获取表的列名
cursorColumnName = conn.cursor()
sqlColumnName = ''' SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME = \'%s\' ''' % (
    DBTABLENAME[0])

cursorColumnName.execute(sqlColumnName)

columnNameTuple = ()
for column in cursorColumnName:
    columnNameTuple = columnNameTuple + column

# 查找数据
cursor = conn.cursor()
sql = ''' SELECT %s FROM %s WHERE ID > %d ''' % (
    ','.join(columnNameTuple), DBTABLENAME[0], MAXGPSADDRESSID)

cursor.execute(sql)

dicRow = {}
for row in cursor:
    # 写入ES中
    for index in range(len(row)):
        dictKey = DBTABLENAME[0] + '_' + columnNameTuple[index]

        if row[index] is None:
            dicRow[dictKey] = ''
        elif isinstance(row[index], datetime):
            dicRow[dictKey] = row[index].strftime('%Y-%m-%dT%H:%M:%S')
        elif isinstance(row[index], str):
            if (columnNameTuple[index] == 'GPSTIME') | (columnNameTuple[index] == 'CURRENTTIME'):
                dicRow[dictKey] = (row[index]).replace(' ', 'T')
            else:
                dicRow[dictKey] = (row[index]).replace(
                    '"', ' ').replace("'", ' ')
        elif isinstance(row[index], cx_Oracle.LOB):
            dicRow[dictKey] = str(row[index]).replace(
                '"', ' ').replace("'", ' ')
        else:
            dicRow[dictKey] = row[index]

    print(dicRow)

    es.index(
        index='tms_gps-sync-address',
        doc_type='tms_gps-sync-address_type',
        body=str(dicRow).replace('\'', '\"'))

cursor.close()
conn.close()


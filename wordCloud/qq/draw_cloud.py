# -*- coding: utf-8 -*-
# wordcloud 分析qq聊天记录

from wordcloud import WordCloud 
import codecs 
import jieba
from scipy.misc import imread
import os
from os import path
import matplotlib.pyplot as plt
from PTL import Image, ImageDraw, ImageFont

def draw_workcloud():
    #读入一个txt文件
    chat_text = open('./zj1258369611.txt', 'r').read()
    cut_text = " ".join(jieba.cut(chat_text))
    d = path.dirname(__file__)
    color_mask = imread("./1.jpg")
    colud = WordCloud(
        background_color = 'white',
        mask = color_mask,
        max_words = 200,
        max_font_size=40
    )

    word_cloud = colud.generate(cut_text)
    word_colud.to_file("./zj.jpg")
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    draw_wordcloud()





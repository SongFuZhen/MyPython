#!/usr/bin/env python
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

# -*- coding: utf-8 -*-

from os import path
from wordcloud import WordCloud
import jieba

d = path.dirname(__file__)

# Read the whole text.
#text = open(path.join(d, './a2.txt')).read()

newtext = []
for word in open('./zj1258369611.txt', 'r'):
    tmp = word[0:4]
    #print(tmp)
    if(tmp == "2017" or tmp == "===="):
        continue
    tmp = word[0:2]
    if(tmp[0] == '[' or tmp[0] == '/'):
        continue
    newtext.append(word)

with open('./a2.txt', 'w') as f:
    for i in newtext:
        f.write(i)
text = open('./a2.txt', 'r').read()
cut_text = " ".join(jieba.cut(text))

# Generate a word cloud image
wordcloud = WordCloud(font_path='./HYQiHei-25J.ttf',background_color = 'white').generate(cut_text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(font_path='./HYQiHei-25J.ttf', max_font_size=40, background_color = 'white').generate(cut_text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
from wordcloud import WordCloud, ImageColorGenerator
import os 
import numpy as np
import PIL.Image as Image

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
word_jieba = jieba.cut(text, cut_all=True)
word_split = " ".join(word_jieba)
alice_coloring = np.array(Image.open(os.open.join('./', './1.jpg')))
my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=alice_coloring, max_font_size=40, random_state=42).generate(word_split)
image_colors = ImageCoorGenerator(alice_coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()



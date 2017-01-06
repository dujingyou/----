# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 18:27:32 2016

@author: 耗子
"""

# Image 模块提供了一个同名类（Image），也提供了一些工厂函数，包括从文件中载入图片和创建新图片
from PIL import Image
from wordcloud import WordCloud
# Matplotlib是一个Python的图形框架，类似于MATLAB和R语言
import matplotlib.pyplot as plt
import codecs

text = codecs.open(u'test.txt','r','utf-8').read()


wordcloud = WordCloud(font_path=('Redocn_2012102302110925.ttf'),
                      background_color="black", margin=5, width=1800, height=800)

wordcloud = wordcloud.generate(text)


plt.figure()
# 以下代码显示图片
plt.imshow(wordcloud)
plt.axis("off")
# 绘制词云
plt.show()

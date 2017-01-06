# coding: utf-8
'''
Created on Tue Dec 27 18:27:32 2016

@author: 耗子
'''
# Image 模块提供了一个同名类（Image），也提供了一些工厂函数，包括从文件中载入图片和创建新图片
from PIL import Image
from os import path
import numpy as np
# Matplotlib是一个Python的图形框架，类似于MATLAB和R语言
# Matplotlib的pyplot子库提供了和matlab类似的绘图API，方便用户快速绘制2D图表
import matplotlib.pyplot as plt
# matplotlib.use('qt4agg')
from wordcloud import WordCloud, STOPWORDS,ImageColorGenerator
import jieba
from scipy.misc import imread

class WordCloud_CN:
    '''
    use package wordcloud and jieba
    generating wordcloud for chinese character
    '''

    def __init__(self, stopwords_file):
        # type: (object) -> object
        self.stopwords_file = stopwords_file
        self.text_file = text_file

    @property
    def get_stopwords(self):
        self.stopwords = {}
        f = open(self.stopwords_file, 'r')
        line = f.readline().rstrip()
        while line:
            self.stopwords.setdefault(line, 0)
            self.stopwords[line.decode('utf-8')] = 1
            line = f.readline().rstrip()
        f.close()
        return self.stopwords

    @property
    def seg_text(self):
        with open(self.text_file) as f:
            text = f.readlines()
            text = r' '.join(text)

            seg_generator = jieba.cut(text)
            self.seg_list = [
                i for i in seg_generator if i not in self.get_stopwords]
            self.seg_list = [i for i in self.seg_list if i != u' ']
            self.seg_list = r' '.join(self.seg_list)
        return self.seg_list

  ###  第二步  修改图片背景
    def show(self):
	    # 设置背景图片 
        coloring = imread(u'./图片/林丹.png')

  ###  可选  字体
        # wordcloud = WordCloud(max_font_size=40, relative_scaling=.5)
        wordcloud = WordCloud(font_path=u'./字体/Redocn_2012102302110925.ttf',#设置字体
							  mask=coloring,#设置背景图片  
                              background_color="white", #背景颜色 
							  margin=5, width=1800, height=800)#生成词云大小
        wordcloud = wordcloud.generate(self.seg_text)
        image_colors = ImageColorGenerator(coloring)


  ###   第三步  生成图片的命名
  
        # 以下代码显示图片
        plt.imshow(wordcloud)
        plt.axis("off")
        # 绘制词云
        plt.show()
        # 保存图片
        wordcloud.to_file(u'./生成/林丹.png')

 ###  第一步  修改读取文本
if __name__ == '__main__':
    stopwords_file = u'./停用词/stopwords.txt'
    text_file = u'./文本/林丹.txt'

    generater = WordCloud_CN(stopwords_file)
    generater.show()

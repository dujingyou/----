# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:13:29 2016

@author: SongKai
"""

import jieba
import numpy
import codecs
import pandas
#import matplotlib.pyplot as plt
#from wordcloud import WordCloud

file = codecs.open("HLM.txt", 'r', 'utf-8')
content = file.read()
file.close()
jieba.load_userdict("HLMwords.txt")


segments = []
segs = jieba.cut(content)
for seg in segs:
    if len(seg)>1:
        segments.append(seg)
        
segmentDF = pandas.DataFrame({'segment':segments})

#移除停用词
stopwords = [w.strip() for w in codecs.open("StopwordsCN.txt","r").readlines()]

segmentDF = segmentDF[~segmentDF.segment.isin(stopwords)]

wyStopWords = pandas.Series([
		  # 42 个文言虚词 
		  '之', '其', '或', '亦', '方', '于', '即', '皆', '因', '仍', '故', 
		  '尚', '呢', '了', '的', '着', '一', '不', '乃', '呀', '吗', '咧', 
		  '啊', '把', '让', '向', '往', '是', '在', '越', '再', '更', '比', 
		  '很', '偏', '别', '好', '可', '便', '就', '但', '儿', 
		  # 高频副词 
		  '又', '也', '都', '要', '一个'
		  # 高频代词 
		  '这', '那', '你', '我', '他',
		  #高频动词
		  '来', '去', '道', '笑', '说',
		  #空格
		  ' ', ''
		]);

segmentDF = segmentDF[~segmentDF.segment.isin(wyStopWords)]
segStat = segmentDF.groupby(
					by=["segment"]
				)["segment"].agg({
					"计数":numpy.size
				}).reset_index().sort(
					columns=["计数"],
					ascending=False
				);
			
print segStat.head(100)


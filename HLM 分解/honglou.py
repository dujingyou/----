# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 18:27:32 2016

@author: 耗子
"""
from os import path
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
		  '又', '也', '都', '要', 
		  # 高频代词 
		  '这', '那', '你', '我', '他',
		  #高频动词
		  '来', '去', '道', '笑', '说',
		  #空格
		  ' ', ''
		]);

segmentDF = segmentDF[~segmentDF.segment.isin(wyStopWords)]
segStat = segmentDF.groupby(by=["segment"])["segment"].agg({"计数":numpy.size}).reset_index().sort(columns=["计数"],ascending=False);
print segStat.head(100)
                            
                            
                            
                            
'''		
lists = []
for i in range(100):
    lists.append(segStat.head(i))


f=codecs.open('新建文本文档1.txt', 'w')
for list in lists:
    f.write(list)
    f.write("\n")
f.close()

f = codecs.open('新建文本文档1.txt', 'r','utf-8')
lines = f.read()


wordcloud = WordCloud(font_path=u'./static/simheittf/simhei.ttf',
                      background_color="black", margin=5, width=1800, height=800)

wordcloud = wordcloud.generate(lists)

plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

'''
# -*- coding: utf-8 -*-
'''
Created on Tue Dec 27 18:27:32 2016

@author: 耗子
'''
import jieba
import numpy
import codecs
import pandas

#import matplotlib.pyplot as plt
#from wordcloud import WordCloud


'''
读取《红楼梦》的文本数据，使用codecs包，
#它可以先通过设置文件的编码，对文件进行读入
'''
file = codecs.open("HLM.txt", 'r', 'utf-8')
content = file.read()
file.close()

'''
1、为了提高分词的准确度，我们最好寻找我们分词的词库，这里我下载到了红楼梦的分词库，加载到jieba中，然后再进行分词。
2、对于小说中，一个字的词，基本上算是无用的词，或者说是标点符号，因此这里我直接抛弃了。
'''
jieba.load_userdict("HLMwords.txt")
segments = []
segs = jieba.cut(content)
for seg in segs:
    if len(seg)>1:
        segments.append(seg)
		
#pandas的DataFrame DataFrame 是一个表格型的数据结构
segmentDF = pandas.DataFrame({'segment':segments})



#移除停用词
stopwords = pandas.read_table(u"StopwordsCN.txt",encoding='utf-8',index_col=False,quoting=3,sep="\t",names=['stopword'])
segmentDF = segmentDF[~segmentDF.segment.isin(stopwords.stopword)]
'''
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
		  ' ', '','\r\n'
		]);

segmentDF = segmentDF[~segmentDF.segment.isin(wyStopWords)]
'''
# pandas聚合和分组运算
segStat = segmentDF.groupby(by=["segment"])["segment"].agg({"计数":numpy.size}).reset_index().sort_values(by=["计数"],ascending=False);
			

print segStat.head(45)
'''
#  pandas.DataFrame.as_matrix      Numpy矩阵/框 转换为Numpy数组

txt = segStat.head(42).as_matrix(columns=None) 
nFile = codecs.open("test.txt", 'w', 'utf-8')
for i in range(42):
    nFile.write(txt[i,0]+"\t")
    nFile.write(str(txt[i,1])+"\r\n")
nFile.close()
'''




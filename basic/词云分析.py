import jieba
import wordcloud
from scipy.misc import imread
mask=imread("2.jpg")
excludes = { }
f=open("1.txt","r",encoding="utf-8")
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=" ".join(ls)
w=wordcloud.WordCloud(font_path="msyh.ttc",width=1000,height=700,background_color="white",max_words=15,mask=mask)
w.generate(txt)
w.to_file("1.png")
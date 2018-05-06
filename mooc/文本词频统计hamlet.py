def  getText():
	txt=open("hamlet.txt","r").read()
	txt=txt.lower()
	for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
		txt=txt.replace(ch," ")
	return txt
hamletTxt=getText()
words=hamletTxt.split()
counts={}
for word in words:
	counts[word]=counts.get(word,0)+1 #核心：有word，把word作为主键，参值+1;如果没有,把word作为主键，get()的返回值为0，加上1，表示第一次出现
items=list(counts.items()) #items()遍历字典转换为列表
items.sort(key=lambda x:x[1],reverse=True)#排序
for i in range(10):
	word,count=items[i]
	print("{0:<10}{1:>5}".format(word,count))
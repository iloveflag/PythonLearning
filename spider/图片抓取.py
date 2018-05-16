import requests
path="D:/abc.jpg"
url="http://img.zcool.cn/community/0142135541fe180000019ae9b8cf86.jpg@1280w_1l_2o_100sh.png"
r=requests.get(url)
print(r.status_code)
with open(path,'wb') as f:
	f.write(r.content)
f.close()
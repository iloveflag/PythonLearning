import requests
from bs4 import BeautifulSoup
url="https://python123.io/ws/demo.html"
r=requests.get(url)
result=r.text
soup=BeautifulSoup(result,"html.parser")
#print(soup.title.parent)
#print(soup.html.parent)
#\print(soup.parent)#None
for parent in soup.a.parents:
	if parent is None:
		print(parent)
	else:
		print(parent.name)

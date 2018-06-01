import requests
from bs4 import BeautifulSoup
url="https://python123.io/ws/demo.html"
r=requests.get(url)
result=r.text
soup=BeautifulSoup(result,"html.parser")
#print(soup.head.contents)
#print(soup.body.contents)
#print(len(soup.body.contents))
#print(soup.body.contents[1])
for child in soup.body.children:
	print(child)
for child in soup.body.descendants:
	print(child)
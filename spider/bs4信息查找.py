import requests
from bs4 import BeautifulSoup
import re#正则表达式库
url="http://python123.io/ws/demo.html"
r=requests.get(url)
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
print(soup.find_all("a"))#返回的是列表类型
print(soup.find_all(["a","b"]))
for tag in soup.find_all(True):
	print(tag.name)

for tag in soup.find_all(re.compile("b")):
	print(tag.name)

print(soup.find_all("p","course"))
print(soup.find_all(id="link1"))
print(soup.find_all(id=re.compile("link")))

print(soup.find_all("a",recursive=False))
print(soup.find_all(string="Basic Python"))
print(soup.find_all(string=re.compile("Python")))
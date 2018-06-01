import requests
from bs4 import BeautifulSoup
url="https://python123.io/ws/demo.html"
r=requests.get(url)
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
print(soup.title)
print(soup.a)
print(soup.a.parent.name)
print(soup.a.attrs["class"])

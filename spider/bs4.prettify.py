import requests
from bs4 import BeautifulSoup
url="https://python123.io/ws/demo.html"
r=requests.get(url)
result=r.text
soup=BeautifulSoup(result,"html.parser")
print(soup.prettify())
print(soup.a.prettify())
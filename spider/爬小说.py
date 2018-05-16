import requests
from bs4 import BeautifulSoup
r=requests.get("https://read.qidian.com/chapter/TtxVU3dYVW81/eSlFKP1Chzg1")
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
result=map(str,soup.select("p"))
result="\n".join(result)
result=result.replace("<p>","")
result=result.replace("</p>","")
with open("test.txt","w") as f:
	f.write(result)
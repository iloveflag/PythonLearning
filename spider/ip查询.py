import requests
url="http://m.ip138.com/ip.asp?ip="
r=requests.get(url+'39.108.146.83')
print(r.text)
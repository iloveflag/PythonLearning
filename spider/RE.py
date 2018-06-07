import re

print("re.search:")
match=re.search(r'[1-9]\d{5}','BIT100081')
if match:
	print(match.group(0))

print("re.match:")
match=re.match(r'[1-9]\d{5}','BIT100081')
if match:
	print(match.group(0))
else:
	print("no match")

print("re.findall:")
ls=re.findall(r'[1-9]\d{5}',"BIT100081 TSU100084")
print(ls)

print("re.split:")
list=re.split(r'[1-9]\d{5}',"BIT100081 TSU100084")
list1=re.split(r'[1-9]\d{5}',"BIT100081 TSU100084",maxsplit=1)
print(list)
print(list1)


print("re.finditer:")
for m in re.finditer(r'[1-9]\d{5}',"BIT100081 TSU100084"):
	if m:
		print(m.group(0))

print("re.sub")
s=re.sub(r'[1-9]\d{5}',":111","BIT100081 TSU100084")
print(s)

print("RE的贪婪匹配:")
match=re.search(r'py.*n',"pyanbncndn")
print(match.group(0))

print("RE的最小匹配:")
match=re.search(r'py.*?n',"pyanbncndn")
print(match.group(0))
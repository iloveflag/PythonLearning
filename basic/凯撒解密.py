#coding:utf-8
c=input()
s=''
l=len(c)
for i in range(l):
        if c[i] in ['x','y','z']:
                s=s+chr(ord(c[i])-23)
        elif ord(c[i])<65 or 90<ord(c[i])<97 or ord(c[i])>122:
          		s=s+c[i]
        else:
                s=s+chr(ord(c[i])+3)
print(s)
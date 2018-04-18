#coding:utf-8
c=input()
s=''
l=len(c)
for i in range(l):
        if c[i] in ['x','y','z']:
                s=s+chr(ord(c[i])-23)
        elif c[i]==' ':
                s=s+' '
        else:
                s=s+chr(ord(c[i])+3)
print(s)

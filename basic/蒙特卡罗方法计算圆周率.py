from random import random
from time import perf_counter
fin=1000*1000
hits=0.0
start=perf_counter()
for i in range(1,fin+1):
  	x,y=random(),random()
  	dist=pow(x**2+y**2,0.5)
  	if dist<=1.0:
  		hits+=1
pi=4*(hits/fin)
print("pi的值是{}".format(pi))
print("运行时间为{:5f}s".format(perf_counter()-start))
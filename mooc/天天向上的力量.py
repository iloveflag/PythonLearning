n=eval(input())/1000
a=pow(1.0+n,365)
b=pow(1.0-n,365)
print("{:.2f},{:.2f},{}".format(a,b,int(a/b)))



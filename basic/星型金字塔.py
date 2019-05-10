x= input()
n=int((eval(x)+1)/2)
for i in range(n):
    a=(i*2+1)*"*"
    print("{}".format(a).center(eval(x)," "))

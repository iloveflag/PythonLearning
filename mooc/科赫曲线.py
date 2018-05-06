import turtle
def koch(size,n):
	if n==0:
		turtle.fd(size)
	else:
		for angle in [0,60,-120,60]:
			turtle.left(angle)
			koch(size/3,n-1)
def main():
	turtle.setup(800,400,-300,-100)
	turtle.pensize(2)
	level=3
	koch(600,level)
	turtle.right(120)
	koch(600,level)
	turtle.right(120)
	koch(600,level)
	turtle.right(120)
	turtle.hideturtle()
main()

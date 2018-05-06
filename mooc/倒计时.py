import time,turtle
turtle.pencolor("blue")
turtle.pensize(10)
turtle.speed(10)
def drawline(draw):
	turtle.pendown() if draw else turtle.penup()
	turtle.fd(80)
	turtle.right(90)
def drawdigit(digit):
	drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
	drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
	drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
	drawline(True) if digit in [0,2,6,8] else drawline(False)
	turtle.left(90)
	drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
	drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
	drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
	turtle.penup()
	turtle.fd(80)
	turtle.left(180)
def drawclean():   
	turtle.pencolor("white")
	for i in range(4):
		drawline(True)
	turtle.left(90)
	for i in range(3):
		drawline(True)
	turtle.penup()
	turtle.fd(80)
	turtle.left(180)
def drawcolor(i):
	if i==9:
		turtle.pencolor("red")
	elif i==8:
		turtle.pencolor("green")
	elif i==7:
		turtle.pencolor("blue")
	elif i==6:
		turtle.pencolor("tan")
	elif i==5:
		turtle.pencolor("pink")
	elif i==4:
		turtle.pencolor("coral")
	elif i==3:
		turtle.pencolor("orange")
	elif i==2:
		turtle.pencolor("black")
	else:
		turtle.pencolor("gray")
def main():
	turtle.write("开始",font=("Arial",60,"normal"))
	time.sleep(1)
	turtle.clear()
	for i in range(9,0,-1):
		drawcolor(i)
		drawdigit(i)
		#drawclean()
		turtle.clear()
	turtle.pencolor("blue")
	turtle.write("结束",font=("Arial",60,"normal"))
	turtle.done()	
main()

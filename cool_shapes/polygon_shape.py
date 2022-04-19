from turtle import *
speed(40)
colors = ['red', 'purple', 'blue', 'green']
# t = turtle.pen()
bgcolor('black')
for x in range(360):
	color(colors[x%4])
	width(x/100)
	forward(x)
	left(59)
done()

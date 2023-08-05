import turtle

colors = ['orange', 'pink', 'red', 'yellow', 'blue', 'green']

screen = turtle.Screen()
trt = turtle.Turtle()
trt.speed(0)
screen.bgcolor('black')

for x in range(360):
    trt.pencolor(colors[x % 6])
    trt.width(x / 5 + 1)
    trt.forward(x)
    trt.left(20)

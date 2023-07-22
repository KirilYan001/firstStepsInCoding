import turtle

colors = ['pink', 'blue', 'red', 'purple']
turtle.speed(50)
turtle.pensize(4)

for i in range(300):
    turtle.color(colors[i % 4])
    turtle.forward(i * 2)
    turtle.left(89)

turtle.done()

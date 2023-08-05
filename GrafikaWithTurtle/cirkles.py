import turtle as tt

tt.Screen().bgcolor('black')
tt.pensize(2)
tt.speed(15)

for i in range(8):
    for color in ('red', 'magenta', 'blue', 'cyan', 'green', 'white', 'yellow'):
        tt.color(color)
        tt.circle(100)
        tt.right(10)

    tt.hideturtle()
tt.done()

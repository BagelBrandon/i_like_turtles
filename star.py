from turtle import *

def draw_star(x, y, points, line, fill):
    penup()
    goto(x, y)
    pendown()

    angle = 180 - (360 / points)

    color(line, fill)
    begin_fill()
    for i in range(points):
        forward(200)
        left(angle)
    end_fill()


bgcolor("black")
speed(100)

draw_star(0, 0, 36, "red", "yellow")
draw_star(0, 0, 36, "yellow", "green")
draw_star(-1050, 50, 4, "red", "red")
draw_star(150, 100, 6, "red", "red")
draw_star(150, 100, 6, "red", "red")


done()

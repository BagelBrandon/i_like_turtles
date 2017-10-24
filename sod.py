from turtle import *

def draw_sod(x, y, points, line, fill):
    penup()
    goto(x, y)
    pendown()

    angle = 120

    color(line, fill)
    begin_fill()
    for i in range(points):
        forward(100)
        right(120)
        forward(100)
        right(120)
        forward(100)
        forward(50)
        right(90)
        forward(60)
        right(90)
        forward(50)
        right(120)
        forward(100)
        right(120)
        forward(100)
        right(120)
        forward(100)

    end_fill()

        
    
speed(65)

draw_sod(0, 0, 36, "red", "blue")


done()


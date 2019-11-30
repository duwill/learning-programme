import turtle

polygon = turtle.Turtle()

num_sides = 10
side_length = 50
angle = 360.0 / num_sides

polygon.begin_fill()

for i in range(12):
    polygon.forward(side_length)
    if(i % 2 == 0):
        polygon.right(60)
    else:
        polygon.left(120)
polygon.color("gray")
polygon.end_fill()

turtle.done()

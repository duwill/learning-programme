import turtle

polygon = turtle.Turtle()

num_sides = int(turtle.textinput('Input', 'Input a number of sides:'))
side_length = 2
angle = 360.0 / num_sides


for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)


turtle.done()
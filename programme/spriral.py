import turtle

spiral = turtle.Turtle()

for i in range(100):
    spiral.forward(i)
    spiral.right(90)

turtle.done()
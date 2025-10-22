import turtle

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.color("Yellow")

for i in range(72):
    pen.forward(100)
    pen.right(60)
    pen.forward(100)
    pen.right(60)
    pen.forward(100)
    pen.right(60)
    pen.forward(100)
    pen.right(60)
    pen.forward(100)
    pen.right(60)
    pen.forward(100)
    pen.right(60)
    pen.right(5)

turtle.done()
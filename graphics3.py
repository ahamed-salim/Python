import turtle

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

for i in range(72):
    pen.color(colors[i % len(colors)])
    pen.circle(100)
    pen.right(5)

turtle.done()
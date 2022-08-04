import turtle

screen = turtle.Screen()
screen.bgcolor("black")

turtle.pensize(1)
turtle.speed(0)


for i in range(8):
    for colors in ["blue", "orange", "yellow", "green", "red", "aqua", "blue", "red"]:
        turtle.color(colors)
        turtle.circle(20)
        turtle.left(6)
        turtle.backward(10)
turtle.done()
turtle.pensize(3)
for i in range(6):
    for colors in ["blue", "red", "green", "blue", "red", "green", "blue", "red"]:
        turtle.color(colors)
        turtle.circle(40)
        turtle.left(20)
        turtle.backward(30)
turtle.done()
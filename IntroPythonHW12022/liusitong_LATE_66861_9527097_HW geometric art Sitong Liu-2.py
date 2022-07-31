from turtle import *

def createSquare():
    forward(150)
    for i in range(3):
        right (90)
        forward(150)
    
    right(5)


for i in range(72):
    createSquare()

exitonclick()
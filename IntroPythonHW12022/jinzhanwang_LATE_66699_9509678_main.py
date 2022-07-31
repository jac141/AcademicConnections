##experiment1
import turtle
shelly = turtle.Turtle()
turtle.bgcolor('black')
colors = ['blue','green','red','yellow','cyan','purple']

for i in range(6):
    shelly.color(colors[i])
    for j in range(4):
        shelly.forward(20)
        shelly.left(90)
    shelly.penup()
    shelly.forward(30)
    shelly.pendown()
shelly.hideturtle()
shelly.clear()

##experiment2
# make a house
turtle.bgcolor('blue')
shelly = turtle.Turtle()
# make the first big square for house
shelly.begin_fill() # start fill of color
shelly.color('gray')
for i in range(4):
  shelly.forward(100)
  shelly.left(90)
shelly.end_fill() # end fill of color
shelly.penup()
shelly.goto(-20,100) # move turtle to next area
shelly.pendown()

# make a red triangle roof
shelly.begin_fill () # start fill for roof
shelly.color('red')
shelly.left(60)
shelly.forward(140)
shelly.right(120)
shelly.forward(140)
shelly.right(120)
shelly.forward(140)
shelly.end_fill() # end fill of color for roof

# make a window
shelly .penup()
shelly.goto(25,80) # move to window position
shelly.pendown()
shelly.begin_fill() # start filling window color
shelly.color('yellow')
for i in range(4):
  shelly.forward(20)
  shelly.left(90)
shelly.end_fill() # end filling window color
shelly.hideturtle()
shelly.clear()
##experiment3

shelly= turtle.Turtle()


shelly.penup()
shelly.goto(0,0)
shelly.pendown()

shelly.begin_fill()
shelly.color('green')
shelly.circle(100)
shelly.end_fill()


shelly.penup()
shelly.goto(-30,100)
shelly.pendown()
shelly.begin_fill()
shelly.color('white')
shelly.circle(30)
shelly.end_fill()
shelly.begin_fill()
shelly.color('black')
shelly.circle(20)
shelly.end_fill()

shelly.penup()
shelly.forward(60)
shelly.pendown()

shelly.begin_fill()
shelly.color('white')
shelly.circle(30)
shelly.end_fill()
shelly.begin_fill()
shelly.color('black')
shelly.circle(20)
shelly.end_fill()
shelly.clear()

##experiment4
turtle.bgcolor('red')
shelly= turtle.Turtle()
shelly.color('black')
for i in range(36):
    shelly.circle(100)
    shelly.right(10)
shelly.clear()

##experiment5
turtle.bgcolor('black')
shelly= turtle.Turtle()
shelly.color('white')
for i in range(36):
    shelly.penup()
    shelly.forward(200)
    for i in range(6):
        shelly.pendown()
        shelly.circle(5)
        shelly.penup()
        shelly.back(20)
    shelly.back(80)
    shelly.right(10)
shelly.hideturtle()
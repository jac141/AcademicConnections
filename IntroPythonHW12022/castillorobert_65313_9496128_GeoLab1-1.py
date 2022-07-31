import turtle 
shelly = turtle.Turtle() 
turtle.bgcolor('black')
colors = ['red','blue','yellow','green','purple','pink','white']
for s in range(0, 6):
  shelly.color(colors[s])
  for i in range(0, 4):
    shelly.forward(20)
    shelly.left(90)
  shelly.penup()
  shelly.forward(30)
  shelly.pendown()

shelly.hideturtle() 
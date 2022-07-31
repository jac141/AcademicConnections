import turtle 
shelly = turtle.Turtle() 
turtle.bgcolor('black')
colors = ['red','blue','yellow','green','purple','pink','white']
for s in range(0,36):
  for i in range(0, 6):
    shelly.forward(100)
    shelly.color(colors[i])
    shelly.left(60)
  shelly.right(10)
shelly.penup() 
shelly.color('white') 
for i in range(0, 36):
  shelly.forward(220) 
  shelly.pendown()  
  shelly.circle(5) 
  shelly.penup() 
  shelly.backward(220) 
  shelly.right(10) 
shelly.hideturtle() 
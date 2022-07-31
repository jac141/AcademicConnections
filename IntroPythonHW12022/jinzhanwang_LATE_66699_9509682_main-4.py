import turtle
shelly = turtle.Turtle()
turtle.bgcolor('black')
colors = ['blue','green','red','yellow','cyan','purple']
for j in range(36):
  for i in range(6):
    shelly.color(colors[i])
    shelly.forward(100)
    shelly.right(60)
  shelly. right(10)

shelly.penup()
shelly.color('white')
for i in range(36):
  shelly.forward(220)
  shelly.pendown() ## otherwise we will get the unnecessary lines
  shelly.circle(5)
  shelly.penup()
  shelly.backward(220)
  shelly.right(10)
  # hide turtle to finish the drawing
shelly.hideturtle()
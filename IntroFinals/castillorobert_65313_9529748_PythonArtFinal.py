import time
import turtle 
shelly = turtle.Turtle() 
turtle.bgcolor('black')
colors = ['red','blue','yellow','green','purple','pink','white']

print("Welcome to the Turtle Art Lab. Please Answer my questions below to get started")
time.sleep(1)
ns = input("How many times would you like the turtle bot to go forwards and to the side? (This can effect how expansionist or isolatory the turtle bot is) This first value can also determine whether or not the turtle bot makes a complete polygon :")
time.sleep(1)
nt = input("Another layer of variety to how spread out or condensed the turtlebot will travel, enter another number :")
time.sleep(1)
fw = input("How far should the turlebot go forward? :")
time.sleep(1)
sdl = input("How far should the turtlebot turn to the left? :")
time.sleep(1)
sdr = input("How far should the turtlebot turn to the right? :")
time.sleep(1)
bgcolor = input("What color do you want the background to be, black or white?")
time.sleep(1)
lncolor = input("What color should the lines be? (red, blue, yellow, green, purple, and pink) :")
time.sleep(1)
print("Thank you, turtlebot should begin drawing shortly.")

turtle.bgcolor(bgcolor)
turtle.speed(10)
for s in range(0, int(nt)):
  for i in range(0, int(ns)):
    shelly.color(lncolor)
    shelly.forward(int(fw))
    shelly.left(int(sdl))
  shelly.right(int(sdr))
shelly.penup()
turtle.hideturtle()


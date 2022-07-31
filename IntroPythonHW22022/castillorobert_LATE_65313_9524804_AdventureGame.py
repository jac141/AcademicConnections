import time

print("You are visiting Santa Cruz, California.")
time.sleep(1)
print("You go on an evening hike alone in the mountains.")
time.sleep(1)
print("You can pick one item to take with you -")
print("A map(m), flashlight(f), chocolate(c), rope(r), or sitcks (s)")
item = input("What do you choose?: ")
time.sleep(1)
print("You hear a humming sound...")
time.sleep(1)
follow = input("Do you follow the sound? :")
if follow == "y":
  print("You keep moving closer to the sound.") 
  time.sleep(1)
  print("The sound suddenly stops.") 
  time.sleep(1)
  print("You are now LOST! ....")   
  time.sleep(1)
  print("You try to call on your phone, but there is no signal!")
  time.sleep(1)
  run = input("What do you do? Keep calling (k) or walk (w)? : ")
  if run != "w":
    print("The phone is not working!")
    time.sleep(1)
    print("Due to your lack of movement, a snake bites you")
    time.sleep(1)
    print("You died XD")
  else:
    direction = input("What direction do you want to walk? North(n), East(e), South(s), or West(w)?")
    if direction == "n":
      print("You reach a cabin")
      if item == "m":
        print("You are able to recollect yourself and find your way back home, you win!!")
      else:
        print("You don't have a way of locating where this cabin is, you lose.")
    elif direction == "e":
      print("You reach a broken bridge")
      if item == "r" or "s":
        print("You were able to repair the bridge and find a trail, you win!!")
      else:
        print("Now you're stuck at this useless bridge; congrats, you've gotten nowhere. You lost.")
    elif direction == "s":
      print("You travel southbound")
      time.sleep(1)
      print("Pfft lol, you just tripped on a log")
      time.sleep(1)
      print("Oh god...")
      time.sleep(1)
      print("Did you really just sprain your ankle?")
      time.sleep(1)
      print("Seriously?")
      time.sleep(1)
      print("Well, you can't move...You lost!")
    elif direction == "w":
      if item == "f":
        print("You were able to flag a car down on the highway with your flashlight and hitch a ride home, nice. You won!")
      else:
        print("As desperately as you may try, no one can see you in this pitch-dark hellhole. Sorry, you lost.")


    
else:
  print("Good idea. You are not taking risks.")
  time.sleep(1)
  print("You start walking back to the starting point.") 
  time.sleep(1)
  print("You realize you are LOST!")
  time.sleep(1)
  print("The sound is behind you and is getting louder. You panic!")
  time.sleep(1)
  print("You look behind you.")
  time.sleep(1)
  print("It's just a silly old woman")
  time.sleep(1)
  print("The old geezer asks, 'What is my favorite programming language?'")
  time.sleep(1)
  lang = input("Well, what is it? :")
  if lang == "python":
    time.sleep(1)
    print("'Hmmm, lucky guess. Well, I'm not a charity, so a ride back home is gonna cost ya. Got any chocolate?''")
    if item =="c":
      time.sleep(1)
      print("She notices you have chocolate in your pocket.")
      time.sleep(1)
      print("'Yum! Let's go then!''")
      time.sleep(1)
      print("The old hag takes you home and you win!")
    else:
      time.sleep(1)
      print("She notices that you don't have chocolate.")
      time.sleep(1)
      print("'Then looks like you're not hitching a ride with Gertrude, buh bye!''")
      time.sleep(1)
      print("You lost AND got humiliated, you suck!")
  else:
    time.sleep(1)
    print("'WRONG!'")
    time.sleep(1)
    print("You lost!")
    

import time
import random

name = input("What's your name: ")

class Player(object):
    def __init__(self):
        self.inGroup = False
        self.hugeManFriends = False
        self.haveScrewdriver = False
        self.doorLocked = True

player = Player()

def Introduction():
    print("-------------------------------------")
    print("Welcome to Prison Break", name + "!")
    print("-------------------------------------")
    time.sleep(1)
    print("You have been incarcerated in a state prison and your only goal is to survive your first day!")
    readyChoiceFunc()

def readyChoiceFunc():
    start = input("CHOICE: are you ready to begin? y/n: ")
    if start == "y":
        print("-------------------------------------")
        print("Good luck", name + "!")
        print("-------------------------------------")
        print("Day 1")
        time.sleep(1)
        print("As you are led to the prison yard you look around and see a huge man, at least 6'6, 300 pounds and covered in tattoos, lifting weights by himself, a group of dudes playing pickup basketball, and an empty bench in the corner away from everything.")
        outsideChoiceFunc()
    elif start == "n":
        print("Goodbye!")
    else:
        print("type 'y' for yes and type 'n' for no ")
        readyChoiceFunc()


def outsideChoiceFunc():
    print("-------------------------------------")
    print("CHOICE: do you want to... ")
    print("A) introduce yourself to the huge man, ")
    print("B) talk to the group playing basketball, ")
    outsideChoiceVar = input("C) sit by yourself on the bench: ")
    
    print("-------------------------------------")
    if outsideChoiceVar == "a":
        print("you greet the man but he doesn't seem to hear you...")
        time.sleep(1)
        print("once he finishes his set you tap his shoulder and he brushes you off, he definitely isn't chatty")
        time.sleep(1)
        print("as you leave you notice he's wearing a golden necklace")
        time.sleep(1)
        print("you walk away")
        outsideChoiceFunc()
    elif outsideChoiceVar == "b":
        print("You wait until they finish their game, then introduce yourself")
        time.sleep(1)
        print("They seem friendly and ask you if you want to join their group")
        groupChoiceFunc()
    elif outsideChoiceVar == "c":
        print("you walk over and sit on the bench, after a couple minutes the basketball group finishes up their game and approaches you")
        time.sleep(1)
        print("They seem friendly and ask you if you want to join their group")
        groupChoiceFunc()
    else:
        print("type 'a' to talk to the huge man, type 'b' to talk to the group playing basketball, and type 'c' to sit by yourself at the bench")
        outsideChoiceFunc()


def groupChoiceFunc():
    print("-------------------------------------")
    print("CHOICE: Do you want to... ")
    print("A) stay solo,")
    groupChoiceVar = input("B) join their group: ")
    print("-------------------------------------")
    if groupChoiceVar == "a":
        print("the group walks away, dissapointed")
        time.sleep(1)
        print("You may have a harder time, but at least you don't owe anybody anything")
        time.sleep(1)
        print("you walk over to the bench and sit until outside time is over")
        time.sleep(1)
        print("-------------------------------------")
        print("outside time is over and you are led to your prison cell, luckily you don't have a cellmate")
        time.sleep(1)
        print("your bed has a metal frame and thin mattress, there is a toilet in sink in the oppisite toilet, you have a wooden chair next to your bed, a large air vent in the middle of the ceiling, and a small barred window above your bed")
        cellChoiceFunc()
    elif groupChoiceVar == "b":
        print("They are happy you want to join them but you have to complete an initiation before you can truly be part of the group")
        time.sleep(1)
        print("the leader says, 'you see the huge man over there lifting weights?'")
        time.sleep(1)
        print("he continues, 'if you can take his golden necklace and give it to us you'll be an official member of our group'")
        initiationChoiceFunc()
    else:
        print("type 'a', if you dont want to join the group, and type 'b' if you want to join the group")
        groupChoiceFunc()


def initiationChoiceFunc():
    print("-------------------------------------")
    print("CHOICE: do you...")
    print("A) still want to join the group")
    initiationChoiceVar = input("B) stay solo: ")
    print("-------------------------------------")
    if initiationChoiceVar == "a":
        print("you agree to go over to the large man and try to take his necklace")
        time.sleep(1)
        print("you walk up behind him and begin to undo the back of the necklace as he does curls")
        stealChance = random.randint(1, 2)
        if stealChance == 1:
            print("the man is too invested in his workout and doesn't notice you taking his necklace")
            time.sleep(1)
            print("the group is satisfied and you play basketball until outside time is finished")
            time.sleep(1)
            player.inGroup = True
            print("they tell you to meet them at the basketball courts first thing tommorow")
            time.sleep(1)
            print("-------------------------------------")
            print("outside time is over and you are led to your prison cell, luckily you don't have a cellmate")
            time.sleep(1)
            print("your bed has a metal frame and thin mattress, there is a toilet in sink in the oppisite toilet, you have a wooden chair next to your bed, a large air vent in the middle of the ceiling, and a small barred window above your bed")
            cellChoiceFunc()
        elif stealChance == 2:
            print("the man notices you taking his necklace and get extremely angry")
            time.sleep(1)
            print("he start hits you in the head and you instantly die.")
    elif initiationChoiceVar == "b":
        print("The group laughs at you and walks away")
        time.sleep(1)
        print("you walk over to the bench and sit until outside time is over")
        time.sleep(1)
        print("-------------------------------------")
        print("outside time is over and you are led to your prison cell, luckily you don't have a cellmate")
        time.sleep(1)
        print("your bed has a metal frame and thin mattress, there is a toilet in sink in the oppisite toilet, you have a wooden chair next to your bed, a large air vent in the middle of the ceiling, and a small barred window above your bed")
        cellChoiceFunc()
    else:
        print("type 'a' if you want to try to steal the necklace or type 'b' if you dont want to steal the necklace")
        initiationChoiceFunc()

def cellChoiceFunc():
    print("-------------------------------------")
    print("CHOICE: do you want to... ")
    print("A) check out the bed")
    print("B) check out the air vent")
    print("C) look out the window")
    if player.doorLocked == False:
      cellChoiceVar = input("D) open the door: ")
    else:
      cellChoiceVar = input("D) open the door (door locked): ")
    
    print("-------------------------------------")
    if cellChoiceVar == "a":
      print("this could be a good place for hiding things, it doesn't look very comfortable though...")
      bedChoiceFunc()
    elif cellChoiceVar == "b":
      print("you look up at the air vent")
      time.sleep(1)
      print("you try to remove it but it has extremely secure screws attaching it to the ceiling...")
      time.sleep(1)
      print("maybe if you had the correct tool you could remove the screws...")
      ventChoiceFunc()
    elif cellChoiceVar == "c":
      if player.haveScrewdriver == False:
        print("you look out the window and see the chainlink fence with barbed wire, you notice you're on the second floor")
        time.sleep(1)
        print("there is a tree branch within arms reach you see a metal point sticking out")
        time.sleep(1)
        print("once you grab it you see it's a screwdriver!")
        time.sleep(1)
        print("*** you have obtained a screwdriver ***")
        if player.haveScrewdriver == False:
          player.haveScrewdriver = True
          cellChoiceFunc()
      else:
        print("you look outside and see it's a beautiful day")
        cellChoiceFunc()
    elif cellChoiceVar == "d":
      if player.doorLocked == True:
        print("you try to open the door but it's locked")
        cellChoiceFunc()
    
    else:
      print("type 'a' if you want to go to the bed, type 'b' if you want to go to the vent, or type 'c' if you want to go to the window")
      cellChoiceFunc()
      
def bedChoiceFunc():
    print("-------------------------------------")
    print("CHOICE: do you want to...")
    print("A) check out the rest of the cell")
    bedChoiceVar = input("B) go to sleep: ")
    print("-------------------------------------")
    if bedChoiceVar == "a":
      print("you walk away from the bed")
      cellChoiceFunc()
    elif bedChoiceVar == "b":
      print("you have survived your first Day!")
      win()
    else:
      print("type 'a' if you want to check out the rest of the cell, or type 'b' if you want to end the day")
      bedChoiceFunc()
      
def ventChoiceFunc():
    print("-------------------------------------")
    print("CHOICE: do you want to... ")
    print("A) check out the rest of the cell, ")
    print("B) yank on the vent to see if it opens")
    if player.haveScrewdriver == True:
        ventChoiceVar = input("C) use screwdriver to open vent: ")
        print("-------------------------------------")
    else:
        ventChoiceVar = input("C) use tool to open vent (not available): ")
        print("-------------------------------------")
    if ventChoiceVar == "a":
      print("you walk away from the vent")
      cellChoiceFunc()
    elif ventChoiceVar == "b":
      print("no matter how hard you yank it the vent won't budge, it does make a lot of noise however")
      time.sleep(1)
      print("you give up")
      ventChoiceFunc()
    elif ventChoiceVar == "c":
      if player.haveScrewdriver == True:
        print("you open the vent and climb along the air ducts until you see the outside world!")
        win()
      else:
        print("this option isn't available")
        ventChoiceFunc()
    else:
      if player.haveScrewdriver == True:
        print("type 'a' to check out the rest of the cell, type 'b' to test if the vent is sturdy, or type 'c' to open the vent using your screwdriver")
        time.sleep(1)
        ventChoiceFunc()
      else:
        print("type 'a' to check out the rest of the cell, or type 'b' to test if the vent is sturdy")
        time.sleep(1)
        ventChoiceFunc()

  
def win():
  print("-------------------------------------")
  print("Congratulations", name, "!")
  print("You have beaten Prison Escape!")
  
Introduction()

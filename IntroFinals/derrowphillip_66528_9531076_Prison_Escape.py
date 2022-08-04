import time
import random

name = input("What's your name: ")

class Player(object):
    def __init__(self):
        self.inGroup = False
        self.hugeManFriends = False
        self.haveScrewdriver = False
        self.haveWireCutters = False
        self.haveGuardsUniform = False
        self.haveRope = False
        self.riot = False
        self.dayCount = 1
        self.itemCount = 0
        self.doorLocked = True
        self.money = 0
        self.groupRep = 0
        self.manRep = 0
        self.beenToBenches = False
        self.beenToBasketball = False
        self.beenToWeights = False
        self.beenToField = False
        self.haveJob = False
        self.janitorTaken = False
        self.washerTaken = False
        self.cafeteriaWorkerTaken = False
        self.painterTaken = False
        self.cookTaken = False
        self.haveWorked = False
        self.janitor = False
        self.washer = False
        self.cafeteriaWorker = False
        self.painter = False
        self.cook = False
        
player = Player()

def Introduction():
    print("-------------------------------------")
    print("Welcome to Prison Break", name + "!")
    print("-------------------------------------")
    time.sleep(1)
    print("You have been incarcerated in a state prison and your only goal is to escape!")
    readyChoiceFunc()

def readyChoiceFunc():
    start = input("CHOICE: are you ready to begin? y/n: ")
    if start == "y":
        print("-------------------------------------")
        print("Good luck", name + "!")
        print("-------------------------------------")
        print("Day", player.dayCount)
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
          player.itemCount += 1
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
        print("you open the door and walk outside")
        print("your in a long hallway lined with cells, not many of them have inmates in them")
        print("to the left you see the yard, and to the right to you see cafeteria")
        hallwayChoiceFunc()
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
      endDay()
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
        print("after a few minutes you successfully open the vent and scramble insde, there is a heavy duty block stopping you from going further, you'll need heavy duty equipment to break through this...")
        time.sleep(1)
        ventChoiceFunc2()
      else:
        print("you need the correct tool to select this choice")
        time.sleep(1)
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

def ventChoiceFunc2():
  print("-------------------------------------")
  print("CHOICE: do you want to... ")
  print("A) climb down and reattach the vent to avoid suspicion")
  if player.haveWireCutters == True:  
    ventChoiceVar2 = input("B) use your wire cutters to remove the heavy duty block: ")
    print("-------------------------------------")
  else:
    ventChoiceVar2 = input("B) use heavy duty tools to remove the heavy duty block (not available): ")
    print("-------------------------------------")
  if ventChoiceVar2 == "a":
    print("you safely get back in your cell and put the vent back where it belongs")
    ventChoiceFunc()
  elif ventChoiceVar2 == "b":
    if player.haveWireCutters == True:
      print("you successfully remove the heavy duty block and climb along the vent for several minutes")
      time.sleep(1)
      print("you see light at the end of the vent and realise it's the outside world")
      time.sleep(1)
      win()
    else:
      print("this option isn't available")
      ventChoiceFunc2()
  else:
    if player.haveWireCutters == True:
      print("type 'a' if you want to return to your cell or type 'b' if you want to remove the heavy duty block with your wire cutters")
      ventChoiceFunc2()
    else:
      print("type 'a' to return to your cell")
      ventChoiceFunc2()

def hallwayChoiceFunc():
  print("-------------------------------------")
  print("CHOICE: do you want to...")
  print("A) go to the left")
  print("B) go to the right")
  hallwayChoiceVar = input("C) go inside your cell: ")
  print("-------------------------------------")
  if hallwayChoiceVar == "a":
    print("you walk down the hallway towards to sunlight streaming from the open doorway, then find youself in the middle of the yard")
    print("around you see an area with benches, a basketball court, an area with weights, and an open field")
    yardChoiceFunc()
  elif hallwayChoiceVar == "b":
    if player.haveJob == False:
      print("you go further inside the prison and see an area to sign up for a job")
      print("you look at the sign up sheet")
      print("-------------------------------------")
      print("JOB SIGN UP SHEET:")
      janitorChance = random.randint(1, 2)
      if janitorChance == 1:
        print("janitor - 15c/d")
      else:
        player.janitorTaken = True
        print("janitor - 15c/d (taken)")
      cafeteriaWorkerChance = random.randint(1, 2)
      if cafeteriaWorkerChance == 1:
        print("cafeteria worker - 20c/d")
      else:
        player.cafeteriaWorkerTaken = True
        print("cafeteria worker - 20c/d (taken)")
      washerChance = random.randint(1, 2)
      if washerChance == 1:
        print("washer - 20c/d")
      else:
        player.washerTaken = True
        print("washer - 20c/d (taken)")
      painterChance = random.randint(1, 2)
      if painterChance == 1:
        print("painter - 25c/d")
      else:
        player.painterTaken = True
        print("painter - 25c/d (taken)")
      if janitorChance == 2 and cafeteriaWorkerChance == 2 and washerChance == 2 and painterChance == 2:
        print("cook - 30c/d")
      else:
        player.cookTaken = True
        print("cook - 30c/d (taken)")
      jobChoiceFunc()
    else:
      print("you arrive at the work station")
      if player.haveWorked == True:
        print("you have already worked today")
        hallwayChoiceFunc()
      else:
        doJobFunc()
  elif hallwayChoiceVar == "c":
    print("you go into your cell")
    cellChoiceFunc()
  else:
    print("type 'a' if you want to the left, type 'b' if you want to go to the right, or type 'c' if you want to go back to your cell")

def doJobFunc():
  print("-------------------------------------")
  doJobVar = input("CHOICE: do you want to work today? y/n: ")
  if doJobVar == "y":
    if player.janitor == True:
      print("you work your job as a janitor and earn 15c!")
      print("you return to the hallway")
      player.haveWorked = True
      player.money += 15
      hallwayChoiceFunc()
    elif player.washer == True:
      print("you work your job as a washer and earn 20c!")
      print("you return to the hallway")
      player.haveWorked = True
      player.money += 20
      hallwayChoiceFunc()
    elif player.cafeteriaWorker == True:
      print("you work your job as a cafeteria worker and earn 20c!")
      print("you return to the hallway")
      player.haveWorked = True
      player.money += 20
      hallwayChoiceFunc()
    elif player.painter == True:
      print("you work your job as a painter and earn 25c!")
      print("you return to the hallway")
      player.haveWorked = True
      player.money += 25
      hallwayChoiceFunc()
    elif player.cook == True:
      print("you work your job as a cook and earn 30c!")
      print("you return to the hallway")
      player.haveWorked = True
      player.money += 30
      hallwayChoiceFunc()
  elif doJobVar == "n":
    print("you leave the job station")
    hallwayChoiceFunc()
  else:
    print("type 'y' if you want to work today or type 'n' if you don't want to work today")
    doJobFunc()

  
def jobChoiceFunc():
  print("-------------------------------------")
  print("CHOICE: what job do you want")
  if player.janitorTaken == False:
    print("A) janitor")
  else:
    print("A) janitor (not available)")
  if player.washerTaken == False:
    print("B) washer")
  else:
    print("B) washer (not available)")
  if player.cafeteriaWorkerTaken == False:
    print("C) cafeteria worker")
  else:
    print("C) cafeteria worker (not available)")
  if player.painterTaken == False:
    print("D) painter")
  else:
    print("D) painter (not available)")
  if player.cookTaken == False:
    jobChoiceVar = input("E) cook: ")
  else:
    jobChoiceVar = input("E) cook (not available): ")
  print("-------------------------------------")
  if jobChoiceVar == "a":
    if player.janitorTaken == False:
      print("you are now a janitor!")
      print("you can start at you job today!")
      player.haveJob = True
      player.janitor = True
      doJobFunc()
    else:
      print("this job isn't available")
      jobChoiceFunc()
  elif jobChoiceVar == "b":
    if player.washerTaken == False:
      print("you are now a washer!")
      print("you can start at you job today!")
      player.haveJob = True
      player.washer = True
      doJobFunc()
    else:
      print("this job isn't available")
      jobChoiceFunc()
  elif jobChoiceVar == "c":
    if player.cafeteriaWorkerTaken == False:
      print("you are now a cafeteria worker!")
      print("you can start at you job today!")
      player.haveJob = True
      player.cafeteriaWorker = True
      doJobFunc()
    else:
      print("this job isn't available")
      jobChoiceFunc()
  elif jobChoiceVar == "d":
    if player.painterTaken == False:
      print("you are now a painter!")
      print("you can start at you job today!")
      player.haveJob = True
      player.painter = True
      doJobFunc()
    else:
      print("this job isn't available")
      jobChoiceFunc()
  elif jobChoiceVar == "e":
    if player.cookTaken == False:
      print("you are now a cook!")
      print("you can start at you job today!")
      player.haveJob = True
      player.cook = True
      doJobFunc()
    else:
      print("this job isn't available")
      jobChoiceFunc()
  else:
    print("type 'a' if you want to be a janitor, type 'b' if you want to be a washer, type 'c' if you want to be a cafteria worker, type 'd' if you want to be a painter, or type 'e' if you want to be a cook")
    jobChoiceFunc()
      
def yardChoiceFunc():
  print("-------------------------------------")
  print("CHOICE: do you want to...")
  if player.beenToBenches == False:
    print("A) go to the benches")
  else:
    print("A) go to the benches (already been today)")
  if player.beenToBasketball == False:
    print("B) go to the basketball court")
  else:
    print("B) go to the basketball court (already been today)")
  if player.beenToWeights == False:
    print("C) go to the area with weights")
  else:
    print("C) go to the area with weights (already been today)")
  if player.beenToField == False:
    print("D) go to the open field")
  else:
    print("D) go to the open field (already been today)")
  yardChoiceVar = input("E) return to the hallway: ")
  print("-------------------------------------")
  if yardChoiceVar == "a":
    if player.beenToBenches == False:
      player.beenToBenches = True
      print("you walk over and sit with a friendly looking group at the benches")
      print("after talking with them for a while they say that they run a shop, and ask you to check out their offers ")
      print("-------------------------------------")
      print("SELLING:")
      if player.money >= 100:
        print("1. Wirecutters - 100c")
      else:
        print("1. Wirecutters - 100c (cannot afford")
      if player.money >= 10:
        print("2. Screwdriver - 10c ")
      else:
        print("2. Screwdriver - 10c (cannot afford)")
      if player.money >= 150:
        print("3. guards uniform - 150c")
      else:
        print("3. guards uniform - 150c (cannot afford)")
      if player.money >= 50:
        print("4. rope - 50c")
      else:
        print("4. rope - 50c (cannot afford)")
      shopChoiceFunc()
    else:
      print("you have already been here today")
      yardChoiceFunc()
  elif yardChoiceVar == "b":
    if player.beenToBasketball == False:
      player.beenToBasketball = True
      if player.inGroup == True:
        player.groupRep += 1
        print("you play basketball with your friends, they remind you that if you need anything they'll help you out")
        print("after a few games you leave and return to the middle of the yard")
        yardChoiceFunc()
      else:
        print("you play shoot hoops by yourself for a while, then return to the middle of the yard")
        yardChoiceFunc()
    else:
      print("you have already been here today")
      yardChoiceFunc()
  elif yardChoiceVar == "c":
    if player.beenToWeights == False:
      player.beenToWeights = True
      if player.hugeManFriends == True:
        print("you see your huge friend working out")
        print("you walk over and work out with him for a while")
        player.manRep += 1
        hugeManChoiceFunc()
      else:
        print("you see the huge man working out")
        weightsChoiceFunc()
    else:
      print("you have already been here today")
      yardChoiceFunc()
  elif yardChoiceVar == "d":
    if player.beenToField == False:
      player.beenToField = True
      print("you walk over to the open field and see a couple people relaxing")
      print("you don't want to distract them so you walk over to the fench and inspect it")
      print("it's the only thing seperating you and the outside world but the wires cannot be cut through")
      print("using rope you could throw it over the fence and climb over, but only if no one notices")
      fieldChoiceFunc()
    else:
      print("you have already been here today")
      yardChoiceFunc()
  elif yardChoiceVar == "e":
    print("you leave the yard and go back to the main hallway")
    hallwayChoiceFunc()
  else:
    print("type 'a' if you want to go to the benches. type 'b' if you want to go the basketball court, type 'c' if you want to go to the weights area, or type 'd' if you want to go to the field")
    yardChoiceFunc()
  
def fieldChoiceFunc():
  print("-------------------------------------")
  print("CHOICE: do you want to...")
  print("A) go back to the yard")
  if player.haveRope == True:
    fieldChoiceVar = input("B) use rope to climb over fence (very risky): ")
  else:
    fieldChoiceVar = input("B) use rope to climb over fence (not available): ")
  print("-------------------------------------")
  if fieldChoiceVar == "a":
    print("you leave the field and return to the middle of the yard")
    yardChoiceFunc()
  elif fieldChoiceVar == "b":
    if player.haveRope == True:
      ropeEscapeChance = random.randint(1, 2)
      if ropeEscapeChance == 1:
        print("you sucessfully climb the rope over the fence and escape without anybody noticing!")
        win()
      else:
        print("the guards see you trying to climb the rope and catch you")
        print("you get moved to a maximum security prison")
        print("GAME OVER")
    else:
      print("option not available")
      fieldChoiceFunc()
  else:
    print("type 'a' if you want to return to the yard, or type 'b' to try to climb over the fence using rope")
    fieldChoiceFunc()
  
def weightsChoiceFunc():
  print("-------------------------------------")
  print("CHOICE: do you want to...")
  print("A) introduce yourself to the huge man")
  print("B) workout by yourself")
  weightsChoiceVar = input("C) leave and go back to the yard: ")
  print("-------------------------------------")
  if weightsChoiceVar == 'a':
    friendChance = random.randint(1, 2)
    if friendChance == 1:
      print("the man seems to like you and you too establish your friendship")
      print("you two work out together then you leave")
      player.hugeManFriends = True
      player.manRep += 1
      yardChoiceFunc()
    else:
      print("the man brushes you off and doesn't seem to want to talk to you")
      print("try again another day")
      yardChoiceFunc()
  elif weightsChoiceVar == 'b':
    print("you workout by yourself for a while, you feel much better")
    print("you finish up then return to the middle of the yard")
    yardChoiceFunc()
  elif weightsChoiceVar == 'c':
    print("you leave the weights area and return to the middle of the yard")
    yardChoiceFunc()
      
def hugeManChoiceFunc():
  print("-------------------------------------")
  print("CHOICE: do you want to...")
  print("A) go back to the yard")
  print("B) ask the man to help you start a riot")
  hugeManChoiceVar = input("C) tell him a joke then leave: ")
  print("-------------------------------------")
  if hugeManChoiceVar == "a":
    print("you say goodbye then go back to the middle of the yard")
    yardChoiceFunc()
  elif hugeManChoiceVar == "b":
    if player.manRep >= 3:
      print("you formulate a plan and he agrees to start it in the middle of the night")
      player.startRiot = True
    else:
      print("the man say he doesn't know you well enough to make such a big move with you")
      print("(try talking to him every day)")
  elif hugeManChoiceVar == "c":
    laughChance = random.randint(1, 2)
    if laughChance == 1:
      print("he laughs at your joke then you guys say goodbye to eachother then you leave")
      player.manRep += 1
      yardChoiceFunc()
    else:
      print("he doesn't laugh at your joke and you awkwardly leave")
      yardChoiceFunc()
  else:
    print("type 'a' if you want to go back to the yard, type 'b' if you want to ask the man to start a riot, or type 'c' if you want to tell the mana joke then leave")
    hugeManChoiceFunc()
       
def shopChoiceFunc():
  print("-------------------------------------")
  print("SHOP: what do you want to buy?")
  shopChoiceVar = input ("type L to leave: ")
  if shopChoiceVar == "1":
    if player.money >= 100:
      print("you have purchased wirecutters!")
      player.haveWireCutters = True
      player.money -= 100
      player.itemCount += 1
      shopChoiceFunc()
    else:
      print("-------------------------------------")
      print("cannot afford")
      shopChoiceFunc()
  elif shopChoiceVar == "2":
    if player.money >= 10:
      print("you have purchased a screwdriver!")
      player.haveScrewdriver = True
      player.money -= 10
      player.itemCount += 1
      shopChoiceFunc()
    else:
      print("-------------------------------------")
      print("cannot afford")
      shopChoiceFunc()
  elif shopChoiceVar == "3":
    if player.money >= 150:
      print("you have purchased a guards uniform!")
      player.haveGuardsUniform = True
      player.money -= 150
      player.itemCount += 1
      shopChoiceFunc()
    else:
      print("-------------------------------------")
      print("cannot afford")
      shopChoiceFunc()
  elif shopChoiceVar == "4":
    if player.money >= 50:
      print("you have purchased a rope!")
      player.haveRope = True
      player.money -= 50
      player.itemCount += 1
      shopChoiceFunc()
    else:
      print("-------------------------------------")
      print("cannot afford")
      shopChoiceFunc()
  elif shopChoiceVar == "l":
    yardChoiceFunc()
  else:
    print("-------------------------------------")
    print("type '1' if you want to purchase wirecutters, type '2' if you want to purchase a screwdriver, type '3' if you want to purchase a guards uniform, or type '4' if you wan to purchase a rope")
    shopChoiceFunc()

def endDay():
  if player.riot:
    print("after you fall asleep you hear distant yelling")
    print("the huge man actually came through and started the riot!")
    print("you hear a resounding snapping sound as every cell door lock deactivated")
    print("he must have made it to the electrical room and deactivated the power!")
    print("*** WARNING *** WARNING *** WARNING ***")
    riotChoice1Func()
  else:
    player.dayCount += 1
    print("the day is finished!")
    print("You have collected", player.itemCount, "item(s)!")
    print("You have", player.money, "c!")
    if player.haveScrewdriver == True:
      print("you collected a screwdriver")
    if player.haveWireCutters == True:
      print("you collected wirecutters")
    print("-------------------------------------")
    print("Day", player.dayCount)
    player.doorLocked = False
    player.beenToBasketball = False
    player.beenToBenches = False
    player.beenToField = False
    player.beenToWeights = False
    player.haveWorked = False
    cellChoiceFunc()
    
def riotChoice1Func():
  riotChoiceVar1 = input("there are timed choices ahead, do you wish to proceed? y/n: ")
  if riotChoiceVar1 == "y":
    player.riot = False
    print("you exit your cell")
    print("to your left you see swarms of inmates running towards the yard")
    print("to your right you see 3 guards sprinting towards you")
    riotChoice2Func()
  elif riotChoiceVar1 == "n":
    player.riot = False
    print("you sit tight in your cell until the riot is over")
    endDay()
  else:
    print("type 'y' if you want to proceed with the timed choices or type 'n' if you want don't want to participate in the riot")
    riotChoice1Func()
    
def riotChoice2Func():
  print("-------------------------------------")
  print("CHOICE: do you want to...")
  print("A) go to the left")
  riotChoice2Var = input("B) go to the right: ")
  print("-------------------------------------")
  if riotChoice2Var == "a":
    print("you scramble down the hall and join the crowd sprinting towards to yard")
  elif riotChoice2Var == "b":
    print("you run straight into the guards and get caught")
    print("you are captured and as punishment for leaving your cell you are moved to a maximum security prison")
    print("GAME OVER")
  
def win():
  print("-------------------------------------")
  print("Congratulations", name, "!")
  print("You have beaten Prison Escape!")
  
Introduction()

import time 

answer = input("Would you like to play the game? (yes/no) ")



if answer == "yes":
   print("Welcome to the forest of despair!")
time.sleep(2)
print("Your objective is to get out of the forest without dying!")
print("Good Luck")  

print("First you must gather all the materials for your trip")
time.sleep(3)
print("You get a rope, a flashlight, and a compass") 
time.sleep(4)
print(" A map comes up to you and says, I will be your map for the journey you can ask me anything you want")
time.sleep(3)
answer = input("You see a place to rest for today do you want to rest?  (Yes/ no)")
if answer == "yes": 
    print("You get a good and long rest for your trip tommorow")
    answer = input("You see a basket of fruit that looks delicous do you want to eat it? (yes/no) ")
if answer =="yes":
    print("You ate the Fruit of POWER")
    time.sleep(5)
    print("You ate the fruit and you feel stronger and more energized. You feel like you can walk for days!")
    time.sleep(6)
    print("On your second day of walking you encounter a huge man eating gorilla right behind you!")
    time.sleep(3)
    answer = input("Do you want to fight the gorilla or run from the gorilla? (fight/flight)")
if answer == "fight":
    print("You fought the gorilla and because of your energized fruit you ate you punch the gorilla in the face and the gorilla ran away!")
    time.sleep(2)
    print("The gorilla dropped a key and you picked up the key ")
    time.sleep(3)
    print("That key may be used for later")
    time.sleep(4)
    answer = input("All of a sudden you see a girl who needs your help because her teddy bear broke (yes/ no)")
if answer == "yes":
    print("You use the rope tie the bear back together ")
    time.sleep(2)
    print("the girl thanks you and just says")
    time.sleep(3)
    print("chicken ")
    time.sleep(4)
    print("You continue walking and you see a giant standing in your way!")
    time.sleep(3)
    print("You ask the map if there is any other way")
    answer = input("The only other way around is to a nearby cave do you want to go? Yes/No")
    if answer =="yes":
      print("You found out it is a cave with multiple puzzels!")
      time.sleep(3)
      print("There is a door and it says what is your favorite food?")
      answer= input("What is your favorite food?")
      time.sleep(4)
      print("That is correct!")
      time.sleep(3)
      print("You walk through the door and there is another door asking another question?")
      answer = input("What is the password")
      if answer == "chicken":
        print("Congrats You GOT OUT of the FOrest of Despair")
        print("You won")

      


  
    
    
    

    

  
else:
    print(" NOOO a man eating rabbit chased you down eating you alive!")
    print("YOU LOST")
  
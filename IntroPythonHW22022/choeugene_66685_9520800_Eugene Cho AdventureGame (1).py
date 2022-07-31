# adventure game
# Step 1
def main():
    print("Hello adventurer! Welcome to the game. Please choose an item! You may choose a sword, bow, or polearn.")
    item = input().strip().lower()
    if item == "sword":
        print("You have chosen the sword.")
    elif item == "bow":
        print("You have chosen the bow.")
    elif item == "polearm":
        print("You have chosen the polearm.")
    else:
        print("That is not a valid item!")
        main()

main()
def main1():
    print("There's a loud sound. Follow the sound?")
    choice1 = input().strip().lower()
    if choice1 == "yes":
        print("You keep moving closer to the sound.")
        print("The sound suddenly stops.")
        print("You are now LOST!...")
        print("You try to call on your phone, but there is no signal!")
    if choice1 == "no":
        print("Good idea. You are not taking risks.")
        print("You start walking back to the starting point.")
        print("You realize you are LOST!")
        print("The sound is behind you and is getting louder. You panic!")
    else:
        print("This is no time to be messing around! Yes or no!?")
        main1()
# Step 2
print("What do you do next? Run or call for help?")
decisions = ["run", "call for help"]
for x in decisions:
    

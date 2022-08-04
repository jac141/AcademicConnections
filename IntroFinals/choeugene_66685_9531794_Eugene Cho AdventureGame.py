# adventure game
# Step 1

print("Hi adventurer! What's your name?")
name = input()
print("Hi " + name + "! So glad you have decided to join us today.")
def main():
    print("Hello" + name + ". Welcome to the game. Please choose an item! You may choose a sword, bow, or polearn.")
    item = input().strip().lower()
    if item == "sword":
        print("You have chosen the sword.")
        return "sword"
    elif item == "bow":
        print("You have chosen the bow.")
        return "bow"
    elif item == "polearm":
        return "polearm"
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
print("The sound is behind you and is getting louder. You panic!")
print("What do you do next? Run or call for help?")
def main2():
    decisions = ["run", "call for help"]
    decision_input = input()
    for x in range(3):
        pass
        if decision_input == "run":
            break
            print("You ran away!")
        elif decision_input == "call for help":
            print("You call for help but no one came. You should run")
            print("You're running out of time!")
        else:
            print("Choose quickly!!!")
print("You stop and catch your breath. You see a lake with three sizes of ripples. There are small, medium, and large ripples. Peek under the water?")
ripples = {
    "small ripple": "It's just raindrops from the cave.",
    "medium ripple": "Someone is underwater!",
    "large ripple": "There's an alligator chasing someone"
}
chosen_ripple = input()
def get_underwater(inputA):
    return input.get(inputA)
get_underwater(input())
        



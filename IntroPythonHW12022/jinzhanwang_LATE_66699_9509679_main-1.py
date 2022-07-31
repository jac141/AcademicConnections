##experiment1 
object = input('Name an object in this room:')
food = input('What kind of food do you like?:')
color = input("What is your favorite color:")
animal = input("Enter a name of a zoo animal:")
print('The',animal,"jumped onto the",color,object,"and flew across the city to eat", food, "at his favorite restaurant.")

##experiment2 
red = input('Enter something plural that is red. Example roses:')
blue = input('Enter something plural that is blue. Example violets:')
love = input("Enter something plural you love. Example puppies:")
verb = input("Enter a verb such as jumping, singing:")
print(red, "are red")
print(blue, "are blue")
print("I like", love)
print('But not as much as I love', verb, "with you!")

##experiment3 
inches = input("Enter distance in inches:")
print(int(inches)*2.54)

weights = input('Enter weight in pounds:')
print(int(weights)/2.2)

temperature = input('Enter temperature in Fahrenheit:')
print((int(temperature)-32)/1.8)

##experiment4
bill = input('What is the total on the bill?:')
tip = input('What % tip would you like to give?:')
people = input('How many people are sharing the bill?:')
bill = int(bill)
tip = int(tip)
people = int(people)
tip_amount = bill*tip/100
print('tip amount per person=', str(tip_amount/people))
total_bill = bill+tip_amount
print("total amount per person=", str(total_bill/people))

##experiment5
length = input('Enter length of the room in feet:')
width = input('Enter width of the room in feet:')
height = input('Enter height of the room in feet:')
door = input('Enter number of doors: ')
windows = input('Enter number of windows:')
wall_area = 2*float(length)*float(height)+ 2*float(width)*float(height)
no_paint_area =15*int(windows)+20*int(door)
paint_area=wall_area-no_paint_area
print('Total surface area to paint', str(paint_area))
gallons = round(paint_area/350,2)
print('Number of gallons of paint needed', str(gallons))
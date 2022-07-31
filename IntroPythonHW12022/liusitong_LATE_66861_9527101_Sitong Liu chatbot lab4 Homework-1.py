total_bill = float(input("What is the total bill: "))
tip = int(input("HOw much tip would you like to give? "))
number_of_people = int(input("How many people are spilitting the bill? "))

payment_per_person = round(float((tip + total_bill)/ number_of_people), 2)

print("Each people will pay", payment_per_person, "\nfloat me aaya to google pay kar diyo bhai LOL")

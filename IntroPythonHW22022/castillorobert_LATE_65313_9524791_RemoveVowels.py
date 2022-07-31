vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
change = [""]

initial = input("Remove the Vowels in these words! :")

result = initial

for x in initial.lower and initial.upper():
    if x in vowels:
        result = result.replace(x, "")

print('Here you go! :', result)


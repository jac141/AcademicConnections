x = list(range(1, 2000)) 
n = str(input("Enter a number: "))
output = [i for i in x if n in str(i)]
print (output)
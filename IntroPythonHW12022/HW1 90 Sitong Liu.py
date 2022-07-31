#exercise 4
l = [i for i in range(10)]
l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l = list(range(10))
l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#exercise5
def maximum(x, y, z):

    if (x >= y) and (x >= z):

        largest = x

    elif (y >= x) and (y >= z):

        largest = y

    else:

        largest = z

    return largest

#excercise6
lst = [20, 10, 20, 1, 100]
a,i = min((a,i) for (i,a) in enumerate(lst))
print(a)
#exercise7
def isOdd(num):
 return (num % 2 != 0)

num = int(input('Enter a number: '))

if isOdd(num):
 print(num,"is an odd number")
else:
 print(num,"is not an odd number")
#excercise8
negativeSet = set()

number = int(input("Enter the Total Negative Set Items = "))
for i in range(1, number + 1):
    value = int(input("Enter the %d Set Item = " %i))
    negativeSet.add(value)

print("Negative Set Items = ", negativeSet)

print("\nThe Negative Numbers in this negativeSet Set are:")
for negaVal in negativeSet:
    if(negaVal < 0):
        print(negaVal, end = "  ")
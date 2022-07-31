def is_perfect_square1(integer):
  root = integer ** 0.5
  if integer/root == integer//root:
    return True
  else:
    return False

def is_perfect_square2(n) :
    i = 1
    while(i * i<= n):
         
        # If (i * i = n)
        if ((n % i == 0) and (n / i == i)):
            return True
             
        i = i + 1
    return False


import math

def is_perfect_square3(integer):
  root = int (math.sqrt(integer) + 0.5)
  if root**2 == integer:
    return True
  return False


assert is_perfect_square1(82) == False
assert is_perfect_square1(81) == True
assert is_perfect_square2(81) == True
assert is_perfect_square2(83) == False
assert is_perfect_square3(81) == True
assert is_perfect_square3(83) == False
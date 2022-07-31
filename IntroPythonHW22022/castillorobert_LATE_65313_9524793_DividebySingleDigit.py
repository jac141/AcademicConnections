
def divisible(number):
  a = number/2
  b = number/3
  c = number/4
  d = number/5
  e = number/6
  f = number/7
  g = number/8
  h = number/9

  if (a - int(a) == 0):
    print("True")
  elif (b - int(b) == 0):
    print("True")
  elif (c - int(c) == 0):
    print("True")
  elif (d - int(d) == 0):
    print("True")
  elif (e - int(e) == 0):
    print("True")
  elif (f - int(f) == 0):
    print("True")
  elif (g - int(g) == 0):
    print("True")
  elif (h - int(h) == 0):
    print("True")
  else:
    print(False)

divisible(1571)
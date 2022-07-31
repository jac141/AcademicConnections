def is_leap_year(integer):
  if integer%4 == 0:
    if integer%400 == 0:
        return True
    if integer%100 == 0:
        return False
    return True
  else:
    return False
    
assert is_leap_year(2016) == True
assert is_leap_year(2000) == True
assert is_leap_year(2013) == False
assert is_leap_year(2018) == False
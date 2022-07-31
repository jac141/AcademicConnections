## funciton1 
def silly_case(in_string):
    return in_string.title().swapcase()
print(silly_case('I love apple'))

## function2 
def dash_stringify(word_list):
    return ' - '.join(word_list)
  
fruits = ['orange', 'lemon','lime']
fruit_string = dash_stringify(fruits)
print(fruit_string)

## fucntion3
import math
def is_perfect_square(number) :
    return math.isqrt(number) ** 2 == number
print(is_perfect_square (119025))

## function4
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

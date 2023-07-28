#!/usr/bin/python3
def make_negative(number):
    if number <= 0:
        return number
    elif number > 0:
        return number - (number * 2)
  

print(make_negative(4))
print(make_negative(-3))
print(make_negative(0))

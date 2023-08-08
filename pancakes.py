#!/usr/bin/env python3
import math

def cook_pancakes(n, m):
    if n == 1:
        print(n * 2)
    if n > 1:
        res = math.ceil((n * 2)/m)
        if res == 1:
            print(res + 1)
        else:
            print(res)



cook_pancakes(40, 288) #2
cook_pancakes(142, 604) #2
cook_pancakes(121, 663) #2
cook_pancakes(1, 2) #2
cook_pancakes(2, 2) #2
cook_pancakes(4, 2) #4
cook_pancakes(4, 3) #3
cook_pancakes(2, 3) #2
cook_pancakes(6, 5) #3
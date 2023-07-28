#!/usr/bin/python3
from math import sqrt

def isPrime(num):
    if(num <= 1):
        return False
    for i in range(2, int(sqrt(num))+1):
        if (num % i == 0):
            return False
    return True 
 
 
#isPrime(0)#False
#isPrime(1)#False
#isPrime(2)#True
#isPrime(3)#True
isPrime(73)#True
isPrime(75)#False
#isPrime(-1)#False

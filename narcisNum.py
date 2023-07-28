#!/usr/bin/python3
def narcissistic( value ):
    num_len = len(str(value)) #returns length of 'value
    nums = [int(i) for i in str(value)] #seperates ints in 'value'
    nums_pow = []
    
    for i in nums:
        nums_pow.append((pow(i, num_len)))
    if int(sum(nums_pow)) == value: return(True)
    elif not int(sum(nums_pow)) == value: return(False)

    
narcissistic(7) #True,
narcissistic(371)#True
narcissistic(122) #False
narcissistic(4887) #False,
# print(narcissistic(7)) #True,
# print(narcissistic(371)) #True
# print(narcissistic(122)) #False
# print(narcissistic(4887)) #False,
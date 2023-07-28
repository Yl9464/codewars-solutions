#!/usr/bin/python3
def high_and_low(numbers):
    nums_str = numbers.split(' ')
    nums_int = []
    
    for n in nums_str:
       nums_int.append(int(n))
    
    nums_sorted = sorted(nums_int)
    results = nums_sorted[-1], nums_sorted[0]
    string = " ".join(map(str,results))

    return string
print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))# 42 -9
print(high_and_low("1 2 3"))#3 1

    # listed = sorted(numbers.split(' '))
    # result = [listed[-1], listed[0]]
    # print(' '.join(result))
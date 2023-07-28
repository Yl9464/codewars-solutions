#!/usr/bin/python3

def array_diff(a, b):
    #removes values from list a, that are present in list b
    for x in a:
        if x in b:
            a.remove(x)
        for z in b:
            if z in a:
                a.remove(z)
    print(a)
  
array_diff([1, -12, 14, -10, 2, -12, 14, -13, -19, 12, -5], [12, 0, -4, 4, 14, -12, -20, 9, -14, -9, -20, -16]) #[1, -10, 2, -13, -19, -5]
array_diff([-20, 13, -2, 20, 8, -20, 5, 7, 4, -8, 9, 17], [-2, -19, 5, 7, -10, 19, 5, 17, 1, 18, 4, -12, -13, 14, 13]) #[-20, 20, 8, -20, -8, 9]
array_diff([1,2], [1]) # [2]
array_diff([1,2,2], [1]) #[2,2]
array_diff([1,2,2], [2]) #[1]
array_diff([1,2,2], []) #[1,2,2]
array_diff([1,2,2], [2]) #[1]
array_diff([1,2,3], [1,2]) #[3]
array_diff([], [1,2]) #
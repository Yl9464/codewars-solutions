#!/usr/bin/python3
def move_zeros(lst):
    zeros = []
    for n in lst[:]:
        if n == 0:
            lst.remove(n)
            zeros.append(n)
    print(lst + zeros)
    
 
#move_zeros([1, 0, 1, 2, 0, 1, 3]) #[1, 1, 2, 1, 3, 0, 0]
move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])
#[9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
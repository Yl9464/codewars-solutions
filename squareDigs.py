#!/usr/bin/python3
def two_sum(numbers, target):
    for i, num in enumerate(numbers):
      comp= target - num
      if comp in numbers and numbers.index(comp) != i:  
        return [i, numbers.index(comp)]
#two_sum([1,2,3], 4)# [0,2]
#two_sum([1234,5678,9012], 14690)# [1,2]

def square_digits(num):
  squared = []
  for n in str(num):
    squared.append(int(n) ** 2)
  x = [str(i) for i in squared]
  res = int(''.join(x))
  return res
  
  

square_digits(9119) #811181
#square_digits(0) #0
#square_digits(765) # 493625

          

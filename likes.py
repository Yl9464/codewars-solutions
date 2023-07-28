#!/usr/bin/env python3
def likes(names):
    result = []
    remaining = []
    length = len(names)
    
    if not names:
        print('no one likes this')
    elif length == 1:
        print(''.join(names) + ' likes this')   
    elif length == 2:
        print(' and '.join(names) + ' like this')
    elif length == 3:
        for name in range(length):
            if name + 1 == length:
                result.append(', '.join(names[:2]) + ' and ' + names[name] + ' like this')
        print(''.join(result))
    elif length > 3:  
        for name in range(length): 
            result.append(', '.join(names[:2]))
            if name > 1:
                remaining.append(names[name])
        print(result[0] + ' and ' + str(len(remaining)) + ' others like this')

        
likes([]) #'no one likes this'
likes(['Peter']) #'Peter likes this'
likes(['Jacob', 'Alex']) #'Jacob and Alex like this'
likes(['Max', 'John', 'Mark']), #'Max, John and Mark like this'
likes(['Alex', 'Jacob', 'Mark', 'Max']) #'Alex, Jacob and 2 others like this'
likes(['Alex', 'Jacob', 'Mark', 'Max', 'Harley', 'Charlie'])
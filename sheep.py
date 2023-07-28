#!/usr/bin/python3

def count_sheep(sheep):
    sheep_count = []
    result = len(sheep)
    
    for t_sheep in sheep:
        if t_sheep == True:
            sheep_count.append(t_sheep)
    return('There are '+ str(len(sheep_count)) + ' in total, not ' + str(result))


print(count_sheep(
[True,  True,  True,  False, True,  True,  True,  True , True,  False, True,  False,
True,  False, False, True ,True,  True,  True,  True , False, False, True,  True]))
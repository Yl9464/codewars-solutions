#!/usr/bin/env python3
# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle
import math

def triangle_type(a, b, c):
    angles = []
    types = {}
    
    if a==b==c:
        print('1')
    elif b==c:
        print('3')
    else:        
        try:
            cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
            cos_B = (c**2 + a**2 -b**2) / (2 * a * c) 
            cos_C = (a**2 + b**2 - c**2) / (2 * a *b)
            
            angle_A = round(math.degrees(math.acos(cos_A)))
            angle_B = round(math.degrees(math.acos(cos_B)))
            angle_C = round(math.degrees(math.acos(cos_C))) 
        except ValueError:
            print('0')
        except ZeroDivisionError:
            print('0')
        else:
            angles.append(angle_A)
            angles.append(angle_B)
            angles.append(angle_C)
    
    for x in range(len(angles)):
        if angles[x] == 90:
            types['right'] = angles[x]
        if angles[x] > 90:
            types['obtuse'] = angles[x]  
        if angles[x] < 90:
            types['acute'] = angles[x]
    
    keys = sorted(types.keys())
    for k, v in types.items():
        if v == 0 or v == 180:
            print('0') 
            break
        if 'right' in keys:
            print('2')
            break
        if 'obtuse' in keys:
            print('3')
            break
        if 'acute' in keys:
            print('1')
            break

triangle_type(7.99999, 4, 4)# 3 - obtuse
triangle_type(3, 3, 0)# 0
triangle_type(8, 6, 7) #1 - Acute [76, 47, 58]
triangle_type(105, 100, 6) # 3 - obtuse [146, 33, 1]
triangle_type(7, 3, 2)# 0 - Not triangle
triangle_type(2, 4, 6) #0 - Not triangle
triangle_type(8, 5, 7)# 1 - Acute [82, 46, 52]
triangle_type(3, 4, 5)# 2 - Right [37, 53, 90]
triangle_type(7, 12, 8) # 3- Obtuse [34, 42, 104]
triangle_type(5,5,5) #1 - Acute [60,60,60]
triangle_type(65,56,33) #2 - right [90, 36, 54]

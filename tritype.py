import math

def triangle_type(a, b, c):
    angles = []
    types = {}
    
    if a==b==c:
        return 1
    elif b==c:
        return 3
    try: 
        cos_A = (b**2 + c**2 - a**2) / (2 * b * c) 
        cos_B = (c**2 + a**2 -b**2) / (2 * a * c) 
        cos_C = (a**2 + b**2 - c**2) / (2 * a *b)
        
        angle_A = round(math.degrees(math.acos(cos_A)))
        angle_B = round(math.degrees(math.acos(cos_B)))
        angle_C = round(math.degrees(math.acos(cos_C))) 
    except ValueError:
        return 0
    except ZeroDivisionError:
        return 0
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
            return 0
        if 'right' in keys:
            return 2    
        if 'obtuse' in keys:
            return 3
        if 'acute' in keys:
            return 1
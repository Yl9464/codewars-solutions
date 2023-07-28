def is_valid_walk(walk):
    directions = {}

    if len(walk) == 10: 
        for d in walk:
            if d in directions:
                directions[d] += 1
            else:
                directions[d] = 1

    keys = list(directions.keys())
    keys.sort()
    directions = {i: directions[i] for i in keys}
    
    if len(directions.keys()) == 2:
        if 5 in directions.values():
            return True
        return False

    elif len(directions.keys()) == 4:
        if directions.get('n') == directions.get('s') and directions.get('e') == directions.get('w'):
            return True
        return False
    else: return False
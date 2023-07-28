#!/usr/bin/python3

def do_math(s):
    #print(s.split())
    dict={}
    res=[]
        #index of i  #i: split sections of 's'
    for index, i in enumerate(s.split()):
        l, n = '', '' # l --> letters n --> integers 
        for j in i: #returns individual characters of i
            if j.isalpha(): #if j is letter... 
                l += j          #...add 'j' value to 'l' variable...
            else:               
                n += j             #...if not letter add 'j'to 'n'
        dict[n] = (l, index) #add 'n' value as key and 'l' w/ its 'index' to dict  
        res.append(n) #add 'n' integers to 'res' array 
    
    #lambda function takes any # of arguments, but can only have one expression
    res = sorted(res, key=lambda x: (dict[x][0], dict[x][1])) #sort 'res' array, using lambda function as key 
    
    #lambda function uses 'x' as argurment. Expression: dict at x index 0, dict at x index 1 (in order of occurance)
    sol = [int(res[0])] #value of first number in 'res' array
    
    for i in range(1, len(res)): #loops for range of 1 to length of 'res' array
        # (i-1)% 4 determines which operation is done
        if(i-1)%4==0:  # (i-1)/4 has no remainder...
            sol.append(sol[-1]+int(res[i]))
        elif (i-1)%4 ==1: #(i-1)/4 has remainder 1...
            sol.append(sol[-1]-int(res[i]))
        elif (i-1)%4==2:  #(i-1)/4 has remainder 2...
            sol.append(sol[-1]*int(res[i]))
        else:
            sol.append(sol[-1]/int(res[i]))
    print(round(sol[-1]))  #round last index of 'sol' to nearest integer              



do_math('24z6 1x23 y369 89a 900b') # [89 900 123 369 246] --> 1299
do_math('24z6 1z23 y369 89z 900b') # [900  369  246 123 89] --> 1414
do_math('10a 90x 14b 78u 45a 7b 34y') # [10 45 14 7 78 90 34] --> 60
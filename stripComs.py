#!/usr/bin/env python3
def strip_comments(strng, markers):
    lines =[] 
    res = []
    
    for l in strng.split('\n'):
        lines.append(l)
    for i in range(len(lines)):
        for m in markers:
            if m in lines[i]:
                o =lines[i].index(m)
                lines[i] = lines[i].replace(lines[i][o:], '')   
    for line in lines:
        res.append(line.rstrip())    
    return('\n'.join(res))  
     
#strip_comments('apples, pears # and bananas\ngrapes\navocado @apples', ['@', '!'])# 'apples, pears # and bananas\ngrapes\navocado'
#strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']) # 'apples, pears\ngrapes\nbananas'
#strip_comments('a #b\nc\nd $e f g', ['#', '$'])# 'a\nc\nd')
#strip_comments(' a #b\nc\nd $e f g', ['#', '$'])# ' a\nc\nd')
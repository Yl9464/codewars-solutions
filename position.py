#!/usr/bin/python3
import string

def alphabet_position(text):
    dict = {}
    seperated = list(text.lower())
    nums = []
    str = []
    i = 1

    for a in list(string.ascii_lowercase):
        dict[a] = i
        i += 1
    for l in seperated:
        for x in dict:
            if l == x:
                nums.append(dict.get(x))
    for num in nums:
        str.append("%s" % num)
    str = ' '.join(str)
    replace = text.replace(text, str)
    return replace
    

print(alphabet_position("The sunset sets at twelve o' clock."))#20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11
print(alphabet_position("The narwhal bacons at midnight."))# "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20
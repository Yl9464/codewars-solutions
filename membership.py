#!/usr/bin/python3
#To be a senior: At least 55 years old and handicap greater than 7
#  (handicaps range from -2 to +26), better  player, lower the handicap.
def open_or_senior(data):
    result = []
    for age, cap in data:
        if  age < 55 or  cap <= 7 :
            result.append('Open')
        if age >= 55 and cap > 7 : 
            result.append('Senior')
    return result

print(open_or_senior([(67, 12), (71, 7), (76, 21), (86, 3)]))
#['Senior', 'Open', 'Senior', 'Open']))
print(open_or_senior([(18, 20), (45, 2), (61, 12), (37, 6), (21, 21), (78, 9)]))
#"Open", "Open", "Senior", "Open", "Open", "Senior"
print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))
#['Open', 'Senior', 'Open', 'Senior']
print(open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)]))
#['Open', 'Open', 'Senior', 'Open']

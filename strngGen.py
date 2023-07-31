#!/usr/bin/env python3
import re
def string_generator(pattern):
    input = ['INC_INT', 'INC_FLOAT', 'INTERVAL', 'PERIODIC']

    
    for pat in pattern.split():
        if '[' in pat:
            tokens = re.findall('\[.*\]', pat)
            print(tokens)

    
string_generator("Hello World[INC_INT]!")
#["Hello World1!", "Hello World2!", "Hello World3!", "Hello World4!", "Hello World5!"]
string_generator("I have [INC_INT=3,2] dogs")
#["I have 3 dogs", "I have 5 dogs", "I have 7 dogs", "I have 9 dogs", "I have 11 dogs", "I have 13 dogs"],
string_generator("[INC_FLOAT=2.3,0.000100]")
#["2.300000", "2.300100", "2.300200", "2.300300", "2.300400", "2.300500", "2.300600", "2.300700", "2.300800", "2.300900", "2.301000", "2.301100"],

#string_generator("Season [PERIODIC=1,4], Episode [INTERVAL=1,4]")
#["Season 1, Episode 1", "Season 1, Episode 2", "Season 1, Episode 3", "Season 1, Episode 4", "Season 2, Episode 1", "Season 2, Episode 2"],
#string_generator("[ INC_INT = 200  ,  3  ], [  INC_FLOAT]")
#["200, 0.1", "203, 0.2", "206, 0.3", "209, 0.4", "212, 0.5", "215, 0.6", "218, 0.7", "221, 0.8", "224, 0.9", "227, 1.0", "230, 1.1", "233, 1.2"]
#string_generator("[INC_INT]hello [INTERVAL =1 ,4], [PERIODIC= 1, 2]")
#["1hello 1, 1", "2hello 2, 1", "3hello 3, 2", "4hello 4, 2", "5hello 1, 3", "6hello 2, 3", "7hello 3, 4", "8hello 4, 4", "9hello 1, 5", "10hello 2, 5", "11hello 3, 6"],
#string_generator("[INC_FLOAT]+[INC_FLOAT=1.2]+[INC_FLOAT = 1.3, 1.0001]")
#["0.1+1.2+1.3000", "0.2+1.3+2.3001", "0.3+1.4+3.3002", "0.4+1.5+4.3003", "0.5+1.6+5.3004", "0.6+1.7+6.3005", "0.7+1.8+7.3006", "0.8+1.9+8.3007", "0.9+2.0+9.3008", "1.0+2.1+10.3009", "1.1+2.2+11.3010", "1.2+2.3+12.3011"],
#string_generator("Testing small floats: [INC_FLOAT=0.000001,0.000000003]")
#["Testing small floats: 0.000001000", "Testing small floats: 0.000001003", "Testing small floats: 0.000001006", "Testing small floats: 0.000001009", "Testing small floats: 0.000001012", "Testing small floats: 0.000001015", "Testing small floats: 0.000001018", "Testing small floats: 0.000001021", "Testing small floats: 0.000001024"],
#string_generator("No Tokens")
#["No Tokens", "No Tokens", "No Tokens", "No Tokens", "No Tokens", "No Tokens", "No Tokens"],
#string_generator("")
#["", "", "", "", "", ""],
#string_generator("[INC_INT]}")
#["1}", "2}", "3}", "4}", "5}", "6}"],




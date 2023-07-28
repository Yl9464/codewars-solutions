#!/usr/bin/env python3
def pig_it(text):
    res = []
    for word in text.split():
        if word[0].isalpha():
            rmv_1 = word.replace(word[0], '', 1)
            char_1 = word[0] + 'ay'
            new_word = rmv_1 + char_1
            res.append(new_word)
        elif word.isalpha() == False: 
           res.append(word)
    print(' '.join(res))
    # for word in text.split():
    #     rmv_1 = word.replace(word[0], '', 1)
    #     char_1 = word[0] + 'ay'
    #     new_word = rmv_1 + char_1
    #     res.append(new_word)
    # print(' '.join(res))
       

#pig_it('Pig latin is cool')#'igPay atinlay siay oolcay'
#pig_it('This is my string')#'hisTay siay ymay tringsay'
pig_it('Hello world !') #'elloHay orldway'
pig_it('Sic transit gloria mundi')#'icSay ransittay loriagay undimay'
#pig_it('Hic et nunc')#'icHay teay uncnay'
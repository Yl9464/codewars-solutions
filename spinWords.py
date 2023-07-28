#!/usr/bin/python3

def spin_words(sentence):
    reversed = []
    for word in sentence.split(' '):
        if len(word) >= 5:
            reversed.append(word[::-1])
        if len(word) < 5: reversed.append(word)
    return ' '.join(reversed)

spin_words("Welcome") #"emocleW"
spin_words("to") #"to"
spin_words("CodeWars") #"sraWedoC"
spin_words("Hey fellow warriors") #"Hey wollef sroirraw"
spin_words("This sentence is a sentence") #"This ecnetnes is a ecnetnes"
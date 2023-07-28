#!/usr/bin/python3
import string
def is_pangram(s):
    words = s.lower().split() #list of words
    letters = []
    alphaLetters = []

    for word in words:
        for l in list(word):
            if l.isalpha():
                letters.append(l)
                letters.sort()
    for l in letters:
        for a in list(string.ascii_lowercase):
            if l == a and l not in alphaLetters:
                alphaLetters.append(l)
    if len(alphaLetters) == 26: return True
    else: return False

print(is_pangram("The quick, brown fox jumps over the lazy dog!")) #True
print(is_pangram("Cwm fjord bank glyphs vext quiz: False should equal True")) #True
print(is_pangram("ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ")) #True
print(is_pangram("1bcdefghijklmnopqrstuvwxyz"))#False
print(is_pangram("Aacdefghijklmnopqrstuvwxyz")) #False






#!/usr/bin/python3
from math import sqrt

def are_you_playing_banjo(name):
	name_capped = name.capitalize()
	letter = 'R'
 	
	if name_capped[0] == letter:
		print(name + ' plays banjo')
	else:
		print(name + ' does not paly banjo')
  
are_you_playing_banjo("martin")#"martin does not play banjo"
are_you_playing_banjo("Rikke")#"Rikke plays banjo"
are_you_playing_banjo("bravo")#"bravo does not play banjo"
are_you_playing_banjo("rolf")#"rolf plays banjo"
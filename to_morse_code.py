# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 12:29:21 2025

@author: akank
"""

'''
We no longer use Morse code to transfer information, but that doesn’t mean you can’t use it in a code challenge. 
Write a function in Python that takes in a string that can have alphanumeric characters in lower or upper case.
The string can also contain any special characters handled in Morse code, including commas, colons, apostrophes,
periods, exclamation marks, and question marks. The function should return the Morse code equivalent for the string.
'''

def morse_code(s):
    morse_dict = {
        'A': '.-','B': '-...','C': '-.-.', 'D': '-..','E': '.',
        'F': '..-.','G': '--.', 'H': '....','I': '..','J': '.---',
        'K': '-.-','L': '.-..','M': '--', 'N': '-.','O': '---','P': '.--.',
       'Q': '--.-','R': '.-.','S': '...', 'T': '-','U': '..-','V': '...-',
       'W': '.--', 'X': '-..-','Y': '-.--','Z': '--..',
       '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',
       '4': '....-',  '5': '.....',  '6': '-....',  '7': '--...',
       '8': '---..',  '9': '----.',
       '.': '.-.-.-', ',': '--..--', '?': '..--..', '\'': '.----.',
       '!': '-.-.--', '/': '-..-.',  '(': '-.--.',  ')': '-.--.-',
       '&': '.-...',  ':': '---...', ';': '-.-.-.', '=': '-...-',
       '+': '.-.-.',  '-': '-....-', '_': '..--.-', '"': '.-..-.',
       '$': '...-..-','@': '.--.-.', ' ': '/'
        }
    res = []
    for i in s.upper():
        if i in morse_dict:
            res.append(morse_dict[i])
    return ' '.join(res)
print(morse_code("Hello"))
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 09:51:16 2025

@author: akank
"""



def minion_game(string):
    # your code goes here
    vowels = "AEIOU"
    k_score = 0
    s_score = 0
    n = len(s)
    for i in range(n):
        if s[i] in vowels:
            k_score += n - i
        else:
            s_score += n - i
    if k_score > s_score:
        print("Kevin",k_score)
    elif s_score > k_score:
        print("Stuart",s_score)
    else:
        print("Draw")
s = 'BANANA'
minion_game(s)
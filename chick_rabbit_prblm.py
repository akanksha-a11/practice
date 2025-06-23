# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 11:40:22 2025

@author: akank
"""

'''
Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?
Hints
Use for loop to iterate all possible solutions.
'''

#c+r=35      (num of heads)
#2c+4r=94     (num of legs)

heads = 35
legs = 94
for c in range(heads + 1):
    r = heads - c
    l = 2 * c + 4 * r
    if l == legs:
        print("Chickens:", c)
        print("Rabbits:", r)
        break

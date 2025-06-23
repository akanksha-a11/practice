# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 12:56:04 2025

@author: akank
"""
'''
In this Python challenge, write a function that’ll accept two numbers. These numbers will represent a position on a tic-tac-toe board. 
They can be 0 through 8, where 0 is the top-left spot, and 8 is the bottom-right spot.These parameters are two marks on the tic-tac-toe board. 
The function should return the number of the spot that can block these two spots from winning the game.
'''

def find_spot(spot1,spot2):
    win_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]]
    for l in win_lines:
        if spot1 in l and spot2 in l:
            for spot in l:
                if spot != spot1 and spot != spot2:
                    return spot
    return None
print(find_spot(0,1))
print(find_spot(0,4))
print(find_spot(0,5))

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 11:39:44 2025

@author: akank
"""

'''
Please write a program which accepts a string from console and print the characters
that have even indexes.
Example: If the following string is given as input to the program:
Plain Text
H1e2l3l4o5w6o7r8l9d
 
Then, the output of the program should be:
Plain Text
Helloworld
'''

s = 'H1e2l3l4o5w6o7r8l9d'
for i in range(len(s)):
    if i % 2 == 0:
        print(s[i],end='')
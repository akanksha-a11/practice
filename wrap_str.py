# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 11:09:29 2025

@author: akank
"""
'''
You are given a string S and width W. Your task is to wrap the string into a paragraph of width.
If the following string is given as input to the program:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Then, the output of the program should be:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
'''


s = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
n = 4
for i in range(0,len(s),n):
    print(s[i:i+n])
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 11:40:42 2025

@author: akank
"""

'''For this challenge, you need to write a function in Python that accepts a string of ASCII characters. 
It should return each character’s value as a hexadecimal string. Separate each byte by a space, 
and return all alpha hexadecimal characters as lowercase.
'''
def ascii_to_hex(s):
    res = []
    for char in s:
        hex_val = format(ord(char), 'x')
        res.append(hex_val)
    return ' '.join(res)
print(ascii_to_hex('hi'))
print(ascii_to_hex('123'))
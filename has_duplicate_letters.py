# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 11:24:28 2025

@author: akank
"""
'''
Create a function in Python that accepts one parameter: a string that’s a sentence. 
This function should return True if any word in that sentence contains duplicate letters and False if not.
'''

def duplicate(sentence):
    words = sentence.split()
    for i in words:
        letters = set()
        for j in i:
            if j in letters:
                return True
            else:
                letters.add(j)
    return False
print(duplicate("black dog"))
print(duplicate("hello world"))


def has_dup(s):
    s = s.split()
    for i in s:
        if len(set(i)) != len(i):
            return True
    return False
s = 'helo world'
print(has_dup(s))
        
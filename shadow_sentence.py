# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 1:31:57 2025

@author: akank
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 11:01:52 2025

@author: akank
"""
'''
For the purpose of this challenge, shadow sentences are sentences where every word is the same length and order but without any of the same letters. 
Write a function that accepts two parameters that may or may not be shadows of each other. The function should return True if they are and False if they aren’t.
An example would be “they are round” and “fold two times,” which are shadow sentences, while “his friends” and “our company” are not because both contain an r.
'''


def shadow_sentence(s1,s2):
    w1 = s1.split()
    w2 = s2.split()
    if len(w1) != len(w2):
        return False
    for i in range(len(w1)):
        if len(w1[i]) != len(w2[i]):
            return False
    letter1 = set(''.join(w1))
    letter2 = set(''.join(w2))
    for l in letter1:
        if l in letter2:
            return False
    return True
print(shadow_sentence("they are round", "fold two times"))
print(shadow_sentence("his friends", "our company"))
print(shadow_sentence("abc","def"))

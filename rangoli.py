# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 11:19:44 2025

@author: akank
"""

'''
You are given an integer, N. Your task is to print an alphabet rangoli of size N. 
(Rangoli is a form of Indian folk art based on creation of patterns.)
Different sizes of alphabet rangoli are shown below:
    
#size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
#size 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
 
Hints
First print the half of the Rangoli in the given way and save each line in a list. Then print the list in reverse order to get the rest.
'''


def rangoli(n):
    alpha = [chr(ord('a') + i) for i in range(26)]
    w = 4 * n - 3
    lines = []
    for i in range(n):
        left = []
        for j in range(n - 1, i, -1):
            left.append(alpha[j])
        center = alpha[i]
        right = []
        for j in range(i + 1, n):
            right.append(alpha[j])
        row = left + [center] + right
        line = '-'.join(row)
        line = line.center(w, '-')
        lines.append(line)
    for i in range(n - 2, -1, -1):
        print(lines[i])
    for i in range(n):
        print(lines[i])

rangoli(3)
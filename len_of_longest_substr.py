# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 13:35:16 2025

@author: akank
"""
'''
Given a string, find the length of the longest substring without repeating characters.

"abcabcbb"

Output: 3


'''
s = input()
max_len = 0
for start in range(len(s)):
    for end in range(start + 1, len(s) + 1):
        sub_str = s[start:end]
        if len(set(sub_str)) == len(sub_str):
            if (end - start) > max_len:
                max_len = end - start
print(max_len)


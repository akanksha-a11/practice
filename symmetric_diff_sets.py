# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 11:37:13 2025

@author: akank
"""

'''
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
Input
The first line of input contains an integer, M.The second line contains M space-separated integers.The third line contains an integer, N.The fourth line contains N space-separated integers.


4
2 4 5 9
4
2 4 11 12
 
Output
Output the symmetric difference integers in ascending order, one per line.

5
9
11
12
 
Hints
Use '^' to make symmetric difference operation.
 
'''
n= 4
s1 = {2, 4, 5, 9}
s2 = {2,4,11,12}
new_s = s1^s2
for i in new_s:
    print(i)
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 11:23:03 2025

@author: akank
"""

'''
You are given a date. Your task is to find what the day is on that date.
Input
A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

08 05 2015
Output
Output the correct day in capital letters.
WEDNESDAY
'''

import datetime

m, d, y = map(int, input().split())
date = datetime.date(y, m, d)
print(date.strftime('%A').upper())

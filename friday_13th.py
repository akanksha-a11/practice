# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 2:46:09 2025

@author: akank
"""

'''
Create a function in Python that accepts two parameters.They’ll both be numbers. 
The first will be the month as a number, and the second will be the four-digit year. 
The function should parse the parameters and return True 
if the month contains a Friday the 13th and False if it doesn’t.
'''

import datetime
def friday_13th(m,y):
    d = datetime.date(y,m,13)
    if d.weekday() == 4: 
        return True
    else:
        return False
print(friday_13th(5, 2025))
print(friday_13th(6, 2025))

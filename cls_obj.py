# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 12:00:14 2025

@author: akank
"""

'''
Define a class Person and its two child classes: Male and Female. 
All classes have a method "getGender" which can print "Male" for Male class and
"Female" for Female class.

 
'''

l1 = [1,3,6,78,35,55]
l2 = [12,24,35,24,88,120,155]
s1 = set(l1)
s2 = set(l2)
print(s1.intersection(s2))



class Person:
    def getGender(self):
        return "Unknown"
class Male(Person):
    def getGender(self):
        return "male"
class Female(Person):
    def getGender(self):
        return "Female"

m = Male()
f = Female()
print(m.getGender())
print(f.getGender())
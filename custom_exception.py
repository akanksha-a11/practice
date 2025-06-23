# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 11:00:17 2025

@author: akank
"""

class InvalidData(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
marks = int(input())
try:
    if marks < 0 or marks > 100:
        raise InvalidData("marks should be between 0 and 100")
    else:
        print("valid marks")
except InvalidData as e:
    print(e)

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 23:55:10 2024

@author: Admin
"""

def ktra_so(n):
    if n<0 and n%2 != 0:
        return -1
    elif n>0 and n%2 == 0:
        return 1
    return 0 
print(ktra_so(4))
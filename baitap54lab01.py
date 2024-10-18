# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 14:19:40 2024

@author: Admin
"""

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b=b, a+b
    print()
fib(2018)
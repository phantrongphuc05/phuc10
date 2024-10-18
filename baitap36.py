# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:06:32 2024

@author: Admin
"""

# bài 1 - slide trang 36 
def tinhtong(*args, **kwargs):
    return sum(args)
def tinhtich(*args, **kwargs):
    tich = 1 
    for i in args:
        tich *= i 
    return tich
if __name__=="__main__":
    ds = [1,2,3,4,5]
    print(tinhtong(*ds))
    print(tinhtich(*ds))
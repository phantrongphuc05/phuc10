# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 23:59:16 2024

@author: Admin
"""

def ktra_gtri():
    n = input("nhập n: ")
    if n.replace('.', '', 1).replace('-', '', 1).isdigit():
        n = float(n)
    if -89 <= n <= 90:
        return n 
    print("Không hợp lệ, nhập lại n")
    return ktra_gtri()
print(ktra_gtri())
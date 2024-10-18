# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 14:22:58 2024

@author: Admin
"""

# Bài 1 - slide 58 ( Bài tập lẻ lab01: 49, 50, 51)
#1/a 
def canbac_n(x,n):
    return x**(1/n)
#1/b
def binhphuong(n):
    if n>0:
        return n**2
    else: 
        return "nhập lại n: "
#1/c
def kiemtra(n):
    return n<0 and n%2 == 0
#1/d 
def ktra_so(n):
    if n<0 and n%2 != 0:
        return -1
    elif n>0 and n%2 == 0:
        return 1
    return 0 
#1/e
def ktra_gtri():
    n = input("nhập n: ")
    #Cách 1, ktra và ép kiểu float
    if n.replace('.', '', 1).replace('-', '', 1).isdigit():
        n = float(n)
    #Cách 2, ktra và ép kiểu số int
    #lstrip: cắt dấu trừ trước 1 chuỗi: -123
    #if n.lstrip('-').isdigit():
        #n = int(n)
    if -89 <= n <= 90:
        return n 
    print("Không hợp lệ, nhập lại n: ")
    return ktra_gtri()
if __name__=="__main__":
    print(canbac_n(8, 3))
    print(binhphuong(3))
    print(kiemtra(-4))
    print(ktra_so(4))
    print(ktra_gtri())
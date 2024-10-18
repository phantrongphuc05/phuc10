# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 13:41:41 2024

@author: Admin
"""
#Tính tổng S = 1 + 2 + ... + n
def tong_mot(n):
    tong = 0 
    for i in range(1, n+1):
        tong+=i  
    return tong 
#Tính tổng S = 12 + 22 + ... + n2
def tong_hai(n):    
    tong = 0
    for i in range(1, n+1):
        tong+=i**2
    return tong
#Tính tổng S = 1 + 1/2 + 1/3 + ... + 1/n
def tong_ba(n):
    tong = 0 
    for i in range(1, n+1):
        tong+=1/i 
    return tong 
#Tính tổng S = 1! + 2! + ... + n!
def tong_bon(n):
    tong = 0
    giaithua =1
    for i in range(1, n+1):
        giaithua *=i
        tong += giaithua
    return tong
#Tính tích S = 1 * 2 * ... * n (n!)
def tong_nam(n):
   giaithua =1
   for i in range(1, n+1):
       giaithua *=i
   return giaithua
if __name__ == "__main__":
    print("S1= ",tong_mot(5))
    print("S2= ",tong_hai(4))
    print("S3= ",tong_ba(3))
    print("S4= ",tong_bon(6))
    print("S5= ",tong_nam(7))

    

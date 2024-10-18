# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:55:47 2024

@author: Admin
"""

# bài 3 - slide 36
import math  
def chuvi_dt(hinh, pheptinh, *args, ** kwargs):
    if hinh == 'hinhvuong':
        canh = args[0]
        return 4*canh if pheptinh == 'chuvi' else canh **2 
    elif hinh == 'chunhat':
        dai = args[0]
        rong = args[1]
        return 2*(dai + rong) if pheptinh == 'chuvi' else dai*rong 
    elif hinh == 'hinhtron':
        bk = args[0]
        return 2*math.pi*bk if pheptinh == 'chuvi' else math.pi*bk 
    else:
        return 'hình không hợp lệ'
if __name__ =="__main__":
    print(' chu vi hình vuông : ', chuvi_dt('hinhvuong', 'chuvi', 4))
    print(' diện tích hình vuông : ', chuvi_dt('hinhvuong', 'dientich', 4))
    print(' chu vi hình chữ nhật : ', chuvi_dt('chunhat', 'chuvi', 4, 3))
    print(' diện tích hình chữ nhật : ', chuvi_dt('chunhat', 'dientich', 4, 3))
    print(' chu vi hình tròn: ', chuvi_dt('hinhtron', 'chuvi', 4))
    print(' diện tích hình tròn: ', chuvi_dt('hinhtron', 'dientich', 4))
          
    
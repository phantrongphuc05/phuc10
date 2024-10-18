# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:25:53 2024

@author: Admin
"""

# bài 2 - slide 36
import math  
def chuvi(hinh, *args, ** kwargs):
    if hinh == 'hinhvuong':
        canh = args[0]
        return 4*canh 
    elif hinh == 'chunhat':
        dai = args[0]
        rong = args[1]
        return 2*(dai + rong)
    elif hinh == 'hinhtron':
        bk = args[0]
        return 2*math.pi*bk
    else:
        return 'hình không hợp lệ'
if __name__ =="__main__":
    print(' chu vi hình vuông : ', chuvi('hinhvuong', 4))
    print(' chu vi hình chữ nhật : ', chuvi('chunhat', 4, 3))
    print(' chu vi hình tròn: ', chuvi('hinhtron',4 ))
    
    
    
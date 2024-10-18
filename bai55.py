# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 01:25:01 2024

@author: Admin
"""
def tinh_chuvi(dai, rong):
    chuvi = (dai+rong)*2 
    return chuvi 
def tinh_dientich(dai, rong):
    dientich = dai * rong
    return dientich 
def ve_hinh(dai, rong):
    for i in range(rong):
        print('*' * dai)
print("Chu vi hình chữ nhật: ",tinh_chuvi(4, 3))
print("Diện tích hình chữ nhật: ",tinh_dientich(5, 3))
print("Hình chữ nhật được vẽ như sau:",ve_hinh(6, 4))

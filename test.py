#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:17:54 2020

@author: gongchaoyun
"""
import cv2
import os
import numpy as np
from Bruce_Gong_exercise1 import count_area

h = 240
w = 420
filepath='cat.420x240.bin'
binfile = open(filepath, 'rb') 
size = os.path.getsize(filepath) 
gray = np.fromfile(binfile, dtype=np.ubyte).reshape(h,w)
a = count_area()
A_out = a.count_areas(filepath,int(h),int(w))
'''
cv2.imshow("showing",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

key = np.unique(gray)
result = {}
for k in key:
    mask = (gray == k)
    y_new = gray[mask]
    v = y_new.size
    result[k] = v
#print(result)
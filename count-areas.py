#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 08:46:50 2020

@author: gongchaoyun
"""

from Bruce_Gong_exercise1 import count_area
import argparse

if __name__ == '__main__':   
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    #parser.add_argument( '--file',required=True,type=str,help='the filename or filepath')
    parser.add_argument('--shape',required=True,nargs=1,type=str, help='the height and width ')
    opt = parser.parse_args()
    h =''
    w=''
    mark = 0
    for i in opt.shape[0]:
        if i ==',':
            mark =1
        if mark == 0:
            h = h+i
        elif i != ',':
            w = w+i
            
    a = count_area()
    A_out = a.count_areas(opt.file,int(h),int(w))
    #print(A_out)
    for i in A_out:
        print (int(i))

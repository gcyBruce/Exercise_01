#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 20:52:25 2020

@author: gongchaoyun
"""

import cv2
import os
import numpy as np

class count_area():
    
    def ReadBin(self,filename,h,w):
        filepath=filename
        binfile = open(filepath, 'rb') 
        gray = np.fromfile(binfile, dtype=np.ubyte).reshape(h,w)
        return gray
    
    def ReadImage(self,filename,h,w):
        image = cv2.imread(filename)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray
    

##used to count how many grayscale levels.
    def all_np(self,arr):
        arr = np.array(arr)
        key = np.unique(arr)
        result = {}
        for k in key:
            mask = (arr == k)
            arr_new = arr[mask]
            v = arr_new.size
            result[k] = v
        return result
    
## used to count areas for each grayscale level.
    def CCA(self,arr,h,w):
        link = {}
        next_label = 1
        label = np.zeros([h,w])
        ## First pass
        for i in range(h):
            for j in range(w):
                if arr[i,j]== 1 :
                    if i > 0 :
                        up = label[i-1,j]
                    else:
                        up = None
                    if j > 0 :
                        left = label[i,j-1]
                    else:
                        left = None
                    
                        
                    if (up == None or up == 0) and (left == None or left == 0):
                        link[next_label] = [next_label]
                        label[i,j] = next_label
                        next_label +=1
                    
                    else:
                        L =[]
                        if up != None and up !=0 :
                            L.append(up)
                        if left != None and left !=0:
                            L.append(left)
                        
                        if len(L)>0:
                            #print(L)
                            label[i,j] = min(L)
                            if L[0] != L[-1]:
                                for n,m in enumerate(link):
                                    total = []
                                    if int(L[0]) in link[m] or int(L[1]) in link[m] :
                                        for value in link[m]:
                                            if not total or value not in total:
                                                total.append(value)
                                                
                                    if int(L[0]) not in total:
                                        total.append(int(L[0]))
                                    if int(L[-1]) not in total:
                                        total.append(int(L[-1]))
                                for n,m in enumerate(link):
                                    if int(L[0]) in link[m] or int(L[1]) in link[m] :
                                        link[m] = total

        #print(len(link))
        #print(label.max())

        ##Second pass
        areas = []
        for i in range(h):
            for j in range(w):
                if arr[i,j]== 1 :
                    if label[i,j] in link:
                        label[i,j] = min(link[label[i,j]])
        for i in range(h):
            for j in range(w):
                if arr[i,j]== 1 :
                    if not areas or label[i,j] not in areas:
                        areas.append(label[i,j])
        return len(areas)
    
    def count_areas(self,filename,h,w):
        if filename[-3:] == 'bin':
            gray = self.ReadBin(filename,h,w)
        elif filename[-3:] == 'png' or filename[-3:] == 'jpg' or filename[-3:] == 'peg':
            gray = self.ReadImage(filename,h,w)

        out = np.zeros([256,1])
        nums = self.all_np(gray)
        for k in nums:
            temp = gray.copy()
            for i in range(h):
                for j in range(w):
                    if gray[i, j] == k:
                        temp[i,j] = 1
                    else:
                        temp[i,j] = 0
            #count = cv2.findContours(temp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            count = self.CCA(temp,h,w)
            #print('A[%d]' %int(k),":",count)
            out[int(k)] = int(count)
        return out

'''
a = count_area()
a.count_areas('shades-of-grey.png',640,640)
a.count_areas('sample.bin',256,256)       
'''       

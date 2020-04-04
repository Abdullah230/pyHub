# -*- coding: utf-8 -*-
"""
@author: Abdullah
@Email: abdullah.khan230@yahoo.com
@Github: https://github.com/Abdullah230
Created on Sat Apr  4 20:52:03 2020
"""

def lpsGenerator(text):
    arr = [0]
    j = 0
    i = j+1
    while i < (len(text)):
        if text[i] != text[j]:
            if j == 0:
                arr.append(j)
                i += 1
            if j != 0:
                j = arr[j-1]
        
        else:
            arr.append(j+1)
            i += 1
            j += 1
    return arr

def kmpSearch(text, key):
    arr = lpsGenerator(key)
    M = len(text)
    N = len(key)
    i = 0 # text pointer
    j = 0 # key pointer
    index = []
    
    while i < M:            
        if text[i] == key[j]:
            i += 1
            j += 1
            
        else:
            if j != 0:
                j = arr[j-1]
            
            else:
                i+=1
                
        if j == N:
            index.append(i-N+1)
            j = 0
    
    return index
# -*- coding: utf-8 -*-
"""
@author: Abdullah
@Email: abdullah.khan230@yahoo.com
@Github: https://github.com/Abdullah230
Created on Mon Apr  6 00:20:03 2020
"""
import pandas as pd

def uniqueValues(text):
    values = []
    for i in text:
        if i in values:
            pass
        else:
            values.append(i)
    return values

def jump(text, letter):
    temp = text+letter
    N = len(temp)
    selected = 0
    for i in range(len(temp)-1):
        if temp[0:i+1] == temp[N-(i+1):N]:
            selected = i+1
        
    return selected

def faTable(text):
    tList = uniqueValues(text)
    temp = ""
    tl = []
    table = []
    for i in range(len(text) + 1):
        tl = []
        for j in range(len(tList)):
            if i == 0 and tList[j] == text[0]:
                tl.append(1)
                
            elif i == 0:
                tl.append(0)
                
            elif i < len(text):
                if tList[j] == text[i]:
                    tl.append(i+1)
                else:    
                    tl.append(jump(temp,tList[j]))
            
            else:
                tl.append(jump(temp,tList[j]))
        
        if i < len(text):
            temp = temp + text[i]
        
        else: 
            temp = ""
        table.append(tl)
            
    return table, tList
            
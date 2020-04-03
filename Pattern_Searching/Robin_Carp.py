# -*- coding: utf-8 -*-
"""
@author: Abdullah Khan
@Email: abdullah.khan230@yahoo.com
@GIthub: https://github.com/Abdullah230
Created on Fri Apr  3 13:55:22 2020

implementation: Robin Carp algorithm
"""

def RecursiveHash(text, p = 256):
    if len(text) != 1:
        return (ord(text[0]) * (p**(len(text)-1))) + RecursiveHash(text[1:len(text)], p)
    else:
        return ord(text[0])

def robin_carp(text, key, mod = 256):
    M = len(text) # Length of the text
    N = len(key) # Length of the pattern
    p = 0 # Hash value of the pattern
    h = 0 # hash value of the text
    index = [] # value of the index where the pattern is found
    tempMismatch = 0
    
    p = RecursiveHash(key, mod)
    h = RecursiveHash(text[0:N], mod)
    
    for i in range(M-N+1):
        if h == p:
            for j in range(N):
                if text[i+j] != key[j]:
                    tempMismatch = 1
            if tempMismatch == 0:
                index.append(i+1)
        
        tempMismatch = 0
        h -= ord(text[i]) * (mod**(N-1))
        h *= mod
        try:
            h += ord(text[i+N])
        except:
            print("Reached End")
            return index        

bismillah = robin_carp("find my name", "name", mod = 10)
# -*- coding: utf-8 -*-
"""
@author: Abdullah
@Email: abdullah.khan230@yahoo.com
@Github: https://github.com/Abdullah230
Created on Fri Apr 10 07:05:53 2020
"""
def boyer_moore(text, key):
    M = len(text)
    N = len(key)
    i = 0
    index = []
    while i < M:
        if text[i] == key[0]:
            j = 1
            diff = 0
            while (diff == 0) and (j < N) and (i+j) < M:
                if key[j] == text[i+j]:
                    j += 1
                    if j == N:
                        index.append(i)
                else:
                    diff = j
            i += j
        else:
            i += 1
    return index
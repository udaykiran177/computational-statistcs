# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 09:27:27 2022

@author: y20cs177
"""

l=list(map(int,input().split()))

dup=[]

for i in l:
    if i in dup:
        continue
    dup.append(i)
print(dup)
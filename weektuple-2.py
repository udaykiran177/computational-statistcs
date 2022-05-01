# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 10:15:24 2022

@author: y20cs177
"""

l1 = [(10, 7), (6, 7), (8, 100), (4, 21)]

l2 = [(1, 3), (2, 1), (9, 7), (2, 17)]

l1.sort()
l2.sort()

for (i,j) in zip(l1,l2):
    if (i[0]==j[0]):
        print('(',i[1],',',j[1],')')
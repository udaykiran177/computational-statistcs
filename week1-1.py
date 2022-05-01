# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 08:28:02 2022

@author: y20cs177
"""

import random

l=list(range(1,101))
le=len(l)
e=random.randrange(1,101)

l.remove(e)

# for i in range(1,100):
#     if l.count(i)==0:
#         print('missing element is :',i)
#         break

mid=le//2

while(mid>0):
    if len(l[mid])==l//2:
        
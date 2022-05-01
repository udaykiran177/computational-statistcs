# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 08:37:30 2022

@author: y20cs177
"""

l=list(map(int,input().split()))
le=len(l)
l.sort()
temp=0
for i in range(1,len(l)):
     if l[i]==l[i-1] and temp!=l[i]:
         temp=l[i]
         print('duplicate element is:',l[i])
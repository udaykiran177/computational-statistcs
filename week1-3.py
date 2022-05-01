# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 08:59:21 2022

@author: y20cs177
"""

def search(e):
    low=0
    high=len(l)-1
    while(low<=high):
        mid=(low+high)//2
        if l[mid]>e:
            high=mid-1
        elif l[mid]<e:
            low=mid+1
        else:
            #print("element found at :",mid)
            return l[mid]
    return -1


n,k=map(int,input().split())

l=list(map(int,input().split()))

temp=[]

for i in l:
    m=search(k-i)
    if (m!=-1):
        temp.append((i,m))
        print('(',i,',',m,')')
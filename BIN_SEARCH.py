# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

l=list(map(int,input().split()))
e=int(input())
low=0
high=len(l)-1

while(low<=high):
    mid=(low+high)//2
    if l[mid]>e:
        high=mid-1
    elif l[mid]<e:
        low=mid+1
    else:
        print("element found at :",mid)
        break

    
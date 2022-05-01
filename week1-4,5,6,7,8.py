# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 09:27:27 2022

@author: y20cs177
"""
#week1-7
l=list(map(int,input().split()))

dup=[]

for i in l:
    if i in dup:
        continue
    dup.append(i)
print('after removing duplicates :',dup)

# week1-8

print('reverse :',dup[::-1])

#week1-4
if len(l)==len(dup):
    print('equal')
else:
    print('not equal') 
    
#week1-5
print('maximum element is :',max(dup))
print('minimum element is :',min(dup))

#week1-6

dup.sort()
m=max(dup)
i=len(dup)-1
while(l[i]==m):
    i-=1
print('second largest number is :',dup[i])
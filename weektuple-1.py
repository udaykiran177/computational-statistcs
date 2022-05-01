# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 09:52:17 2022

@author: y20cs177
"""
#weekstring-1
# s=input('enter the string :')
# e=input('enter the character :')
# s1=''
# for i in s:
#     if i==e:
#         continue
#     s1+=i
# print(s1)

l = [(6, 24, 12), (60, 12, 6), (12, 18, 21)]
k=int(input('enter number :'))
c=-1
for i in l:
    for j in i:
        if  j%k!=0:
            c=0
            continue
    if (c==-1):
        print(i)
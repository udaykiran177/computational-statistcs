# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 10:21:54 2022

@author: y20cs177
"""


def orangecap(d):
    m={}
    for i in d:
        for j in d[i]:
            if j not in m:
                m[j]=d[i][j]
            else:
                m[j]+=d[i][j]
    return (m)
d={}
#n=int(input('enter the number:'))
# for i in range(n):
#     temp={}
#     for j in range(n):
#         temp[input('enter the name :')]=input('enter the score :')
#     d[input('enter the test name :')]=temp

m=orangecap({'test1':{'Dhoni':74, 'Kohli':150}, 'test2': {'Dhoni':29, 'Pujara':42}})

max=0
s=''

for i in m:
    if (max<m[i]):
        max=m[i]
        s=i
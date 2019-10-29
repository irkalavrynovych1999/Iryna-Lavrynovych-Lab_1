# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 21:14:55 2019

@author: Ира
"""

import math
print("x1= ")
x1=int(input())
print("y1= ")
y1=int(input())

print("x2= ")
x2=int(input())
print("y2= ")
y2=int(input())

print("x3= ")
x3=int(input())
print("y3= ")
y3=int(input())

print("x4= ")
x4=int(input())
print("y4= ")
y4=int(input())

AB=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
BC=math.sqrt(((x3-x2)**2)+((y3-y2)**2))

AC=math.sqrt(((x3-x1)**2)+((y3-y1)**2))
BD=math.sqrt(((x4-x2)**2)+((y4-y2)**2))
print("AC=")
print(round(AC,3))
print("BD=")
print(round(BD,3))

p=(AB+BC+AC)/2

s=math.sqrt(p*(p-AB)*(p-BC)*(p-AC))
S=s*2
print(round(S,3))

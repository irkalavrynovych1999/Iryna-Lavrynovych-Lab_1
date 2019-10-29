# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 21:20:12 2019

@author: Ира
"""

import math
 
print("Введіть координати центра та радіус сфери")
x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))
r = float(input("R = "))
print("Введіть координати точки")
a= float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
r_xy = math.sqrt((a-x)**2 + (b-y)**2 + (c-z)**2)
 
if r_xy <= r:
	print("Точка належить внутрішній області сфері")
else:
	print("Точка не належить внутрішній області сфері")
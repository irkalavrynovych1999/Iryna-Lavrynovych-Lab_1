# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 21:19:42 2019

@author: Ира
"""

print("кількість років n=")
n=int(input())
print("відсоткова ставка r=")
r=int(input())
print("початковий внесок р=")
p=int(input())

S=p*((1+(r*0.01))**n)
print("S=")
print(S)

# -*- coding: utf-8 -*-
"""
Created on Tue May  9 08:33:53 2023

@author: teodo
"""
import math
import sympy as sp
import matplotlib.pyplot as plt
g= 9810.0

#I mm
d=12.567 #Areal av bunnhull
a=3334.664 #Areal av topphull

h=146.0 #Høyden av boks

h_verider=[]
t_verider=[]
#def h(t):
 #   global h
    
    #return(-1*(math.sqrt(2*g))*(d/a)*math.sqrt(h))

count =0
while h>0 and count <=10000:
    h_verider.append(h)
    t_verider.append(count)  
    Del1=(-1*(math.sqrt(2*g)))
    Del2=d/a
    Del3=math.sqrt(h)
    AHHHAHAH=Del1*Del2*Del3
   # print(AHHHAHAH, count)
    h=h+AHHHAHAH
    #print (h, count)
    count+=1
print(count)
plt.stackplot(t_verider,h_verider)

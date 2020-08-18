# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:11:01 2020

@author: user
"""
import turtle
 
OUO = turtle.Turtle()
cir = int(input("YOUR CIRCLE :"))

for i in range(cir):
    OUO.forward(30)
    OUO.left(360/cir)
    
turtle.done()
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:06:14 2020

@author: user
"""

import turtle
import time
 
OUO = turtle.Turtle()
turtle.penup()
size = 20 
for i in range (30):
    OUO.stamp()
    size = size +3
    OUO.forward(size)
    OUO.right(24)
    
turtle.done
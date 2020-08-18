# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 15:33:49 2020

@author: user
"""

import turtle
import time
 
OUO = turtle.Turtle()
OAO = turtle.Turtle()
OUO.pensize(20)
OAO.pensize(10)
screen = turtle.Screen()
screen.title("THE ART OF OUO!!!!")

OUO.color("blue")
OAO.color("yellow")

for i in range (360):
    OUO.forward(1)
    OUO.left(1)
    OAO.forward(1)
    OAO.left(1)



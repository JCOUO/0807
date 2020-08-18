# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:01:43 2020

@author: user
"""

import random
num = random.randint(1,20)
i=0
while i<5:
    ans = int (input("YOUR NUM :"))
    if ans == num :
        print("YEEEEEP OUO")
        print(i+1)
        break
    elif ans < num:
        print("NOPE")
        print("BIGGER")
    elif ans > num:
        print("NOPE")
        print("TOOOOOOOOO BIG")
        
    i=i+1
    
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:09:03 2020

@author: user
"""

import turtle
n = int(input("輸入邊："))
a = turtle.Turtle()

for i in range(n):
    a.forward(100)
    a.right(360/n)
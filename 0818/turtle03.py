# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 15:33:53 2020

@author: user
"""
import turtle
import time

a = turtle.Turtle()
b = turtle.Turtle()

a.color("yellow")
b.color("pink")

a.pensize(10)
b.pensize(20)

for i in range(360):
    a.forward(1)
    a.right(1)
    b.forward(-1)
    b.right(1)
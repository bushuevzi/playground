#!/usr/share/anaconda3/bin/python3.5
# -*- coding: utf-8 -*-
"""
Created on 01.11.2017

@author: Bushuev Zakhar

Description: Draw circle

"""
########################
# import block
########################
import math
import turtle

########################
# def block
########################

def drawCircleTurtle(x,y,r):
    #move to the start of circle
    turtle.up()
    turtle.setpos(x+r, y)
    turtle.down()

    #draw the circle
    for i in range(0, 365, 5):
        a = math.radians(i)
        turtle.setpos(x+r*math.cos(a), y+r*math.sin(a))

########################
# main block
########################
def main():
    drawCircleTurtle(100, 100,300)
    turtle.mainloop()

if __name__ == '__main__':
    main()

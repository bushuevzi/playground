#!/usr/share/anaconda3/bin/python3.5
# -*- coding: utf-8 -*-
"""
reated on 01.11.2017

@author: Bushuev Zakhar

Description: Эмуляция спинографа

"""
########################
# import block
########################
import math
import turtle
from math import gcd

########################
# def block
########################

# a class that draws a Spirograph
class Spiro:
    # constructor
    def __init__(self, xc, yc, col, R, r, l):
        # create the turtle object
        self.t = turtle.Turtle()
        # set the cursor shape
        self.t.shape('turtle')
        # set the step in degrees
        self.step = 5
        # set the drawindg complete flag
        self.drawingComplete = False
        
        # set the parameters
        self.setparams(xc, yc, col, R, r, l)

        # initialize the drawing
        self.restart()

    # set parameters
    def setparams(self, xc, yc, col, R, r, l):
        # the Spirograph parameters
        self.xc = xc
        self.yx = yc
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col

        # reduce r/R to its smallest form by dividing with the GCD
        gcdVal = gcd(self.r, self.R)
        self.nRot = self.r//gcdVal
        # get ratio of radii
        self.k = r/float(R)
        # set the color
        self.t.color(*col)
        # store the current angle
        self.a = 0

    # restart the drawing
    def restart(self):
        # set the flag
        self.drawingComplete = False
        # show the turtle
        self.showturtle()
        # go to the first point
        self.t.up()
        R, k, l = self.R, self.k, self.l
        a = 0.0
        x = R((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = R((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc+x, self.yc+y)
        self.t.down()

    # draw the whole thing
    def draw(self):
        # draw the rest of the points
        R, k, l = self.R, self.k, self.l
        for i in range(0, 360*self.nRot+1, self.step):
            a = math.radians(i)
            x = R((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
            y = R((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
            self.t.setpos(self.xc+x, self.yc +y)
        # drawing is now done so hide the turtle cursor
        self.t.hideturtle()

    # update by one step
    def update(self):
        # skip the rest of the stap if done
        if self.drawingComplete:
            return
        # increment the angle
        self.a += self.step
        # draw a step
        R, k, l = self.R, self.k, self.l
        # set the angle
        a = math.radians(self.a)
        x = R((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = R((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc+x, self.yc+y)
        # if drawing is complete, set the flag
        if self.a > 360*self.nRot:
            self.drawingComplete = True
            # drawing is now done so hide the turtle cursor
            self.t.hideturtle()

########################
# main block
########################
def main():
    pass

if __name__ == '__main__':
    main()

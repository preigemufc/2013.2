# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 18:01:53 2013

@author: Renato
"""
from __future__ import division
from numpy import *
from pylab import *


def cobweb(f,start,end,p,x0,steps=10,smoothness=100):
    xv = linspace(start,end,smoothness)
    plot(xv,f(xv,p),color='b')
    plot(xv,xv,color='g')
    plot([xv[0],xv[len(xv) - 1]],[0,0],color='k')
    x = zeros(steps)
    x[0] = f(x0,p)
    plot([x0,x0],[0,x[0]],color='r')
    plot([x0,x[0]],[x[0],x[0]],color='r')
    for i in range(steps-1):
        x[i+1] = f(x[i],p)
        plot([x[i],x[i]],[x[i],x[i+1]],color='r')
        plot([x[i],x[i+1]],[x[i+1],x[i+1]],color='r')
    show()        

def f(x,c):
    return x**2 + c

cobweb(f,-2,2,.05,.7)
cobweb(f,-2,2,.05,.9)
cobweb(f,-2,2,.05,.95)

# Examples:
#def f(x,a):
#    return a*x*(1-x)
#def g(x,a):
#    r,k = (a[0],a[1])
#    return x*exp(r*(1-x/k))

#cobweb(g,0,100,[4,20],23,50) # chaos
#cobweb(g,0,30,[2,20],2,30) #periodic
#cobweb(f,0,1,2,.8,20) #fixed

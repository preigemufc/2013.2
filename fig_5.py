# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 05:33:02 2013

@author: Renato
"""
from numpy import *
from pylab import *
import math as m

def x_1(c): 
    return (1 - sqrt(1 - 4*c))/2.

def x_2(c):
    return (1 + sqrt(1 - 4*c))/2.

c = linspace(-.75,.25,100)
plot(c,x_1(c),'b')          # 'b' é um argumento opcional 
plot(c,x_2(c),'--b')        # 'b--' quer dizer "linha tracejada azul"
xlabel('$c$',fontsize=30)   # rótulos dos eixos x e y, tipografados
ylabel('$x^*$',fontsize=30) # e com tamanho de fonte personalizado.

dx = .19
for i in linspace(-.75+dx,.4+dx,5):
    for j in linspace(-.5+dx,1.5+dx,5):
        if m.isnan(x_2(i)):
            arrow(i,j,0,.05,head_width=.03,overhang=1)
        elif j > x_2(i):
            arrow(i,j,0,.05,head_width=.03,overhang=1)
        elif j > x_1(i):
            arrow(i,j,0,-.05,head_width=.03,overhang=1)
        else:
            arrow(i,j,0,.05,head_width=.03,overhang=1)
            
show()

    

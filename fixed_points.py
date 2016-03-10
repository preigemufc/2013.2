# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:39:52 2013

@author: Renato
"""
from __future__ import division
import sympy as sy

x,c = sy.symbols('x c')

f = lambda x,c: x**2 + c
F_x = f(x,c)
F2_x = f(F_x,c)

roots = sy.solve(sy.Eq(F_x,x),x)
rootsl = sy.lambdify(c,roots,'numpy')
 
roots2 = sy.solve(sy.Eq(F2_x,x),x)
rootsl2 = sy.lambdify(c,roots2,'numpy')

c1 = linspace(-2,-3/4,100)
x_s = [rootsl2(i) for i in c1]

for i in xrange(4):
    plot(c1,[j[i] for j in x_s],'b' if i == 0 or i == 1 else '--b')

c2 = linspace(-3/4,1/2,100)
x_1 = lambda c: (1 - sqrt(1 - 4*c))/2
x_2 = lambda c: (1 + sqrt(1 - 4*c))/2
plot(c2,x_1(c2),'b')           
plot(c2,x_2(c2),'--b')
xlabel('$c$',fontsize=30)
ylabel('$x^*$',fontsize=30)

ahow()
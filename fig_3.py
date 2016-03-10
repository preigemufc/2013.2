# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 02:12:56 2013

@author: Renato
"""
from numpy import *
from pylab import *

def f(x0,c,n):
    x=zeros(n)
    x[0] = x0
    for i in range(1,n):
        x[i] = x[i-1]**2 + c
    return x 

t = 10
plot(range(t),f(.5,.05,t))
show()

# f(x0,c,n) é uma função que é iterada n vezes sobre
# o valor inicial x0, possuindo um parâmetro ajustável
# c.

# x = zeros(n) declara um vetor de tamanho n que guardará
# os n valores x0, x1, ..., xn da órbita de x0.

# À cada iteração do loop, a função F(x) = x**2 + c será
# iterada sobre a posição anterior x[n - 1]. O comando
# range(1,n) gera uma lista iniciada em 1 porque a posição
# x[0] já está determinada pelo nosso valor inicial.

# t = 10 declara a quantidade de passos que calcularemos, e
# logo abaixo plotamos a função f com valor inicial
# x0 = 0.5, parâmetro c = 0.05 iterada por t = 10 passos.

# Para o tutorial
#subplot(2,2,1)
#plot(range(t),f(.5,.05,t)) 
#subplot(2,2,2)
#plot(range(t),f(.7,.05,t)) 
#subplot(2,2,3)
#plot(range(t),f(.9,.05,t)) 
#subplot(2,2,4)
#plot(range(t),f(.955,.05,t)) 
#show()
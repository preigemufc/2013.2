# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 02:11:34 2013

@author: Renato
"""

# Este é um comentário. Tudo o que estiver escrito após o "#"
# será ignorado pelo interpretador.

from numpy import *
from pylab import *

# Antes de mais nada, carregamos o pacote de funções 
# matemáticas "numpy" e o pacote de criação de gráficos 
# "matplotlib", que é distribuído sob o nome de "pylab".

def f(x,c):
    return x**2 + c 

# "def f(x,c)" é a sintaxe de declaração de uma função chamada
# "f" que recebe "x" e "c" como argumentos. ":" denota que há um
# bloco de comandos a partir da linha seguinte, pertencente à
# função "f". Neste caso, o bloco é formado por apenas um comando:
# retorne o valor de x**2 + c, lembrando que x**2 é a sintaxe do
# Python para a função quadrado. 

x = np.linspace(-2,2,30)

# A função "linspace(a,b,c)" retorna um vetor de (a + b)/c
# elementos, iniciando em "a", terminando em "b", espaçados
# por "c". Ela gera a sequência de valores de x que vamos passar
# à função para plotagem. 

plot(x, f(x,.05))

# A função "plot(a,b)" plota o vetor "b" contra o vetor "a",
# ambos de mesmo tamanho, na forma de pontos {(a1,b1),...,(an,bn)}
# se a = [a1,...,an] e b = [b1,...,bn]. O comando "f(x,.5)"
# gera um vetor de 30 elementos que corresponde à imagem do
# vetor "x" sob a função "f".
plot([0,2],[0,2])
show()

# Já que o Python não mostra instantaneamente os gráficos
# gerados, precisamos pedir para que eles sejam mostrados
# através do comando "show". 
#Daniel Ferreira
import numpy as np

#1)
def senoPositivo(a:int , b:int , n:int) -> np.vectorize:
    '''função consiste em devolver os números onde o seno deles são positivos.'''
    c = np.linspace(a , b , n)
    d = np.sin(c) > 
    return c[d]
  
#2)
def polinomio(vetor: np.vectorize, z:int) -> int:
    '''A função recebe um vetor e um número nisso, ela retorna a soma de um polinomio, com eles sendo multiplicado pela váriavel Z e elevados pelo a posição começando em 0'''
    a = np.comprod(z * np.ones(len(vetor)-1))
    b = np.linspace(1 ,len(vetor)-1 ,len(vetor)-1 )
    c = np.cumsum(vetor[b] * a)
    return c.max() + vetor[0]






    
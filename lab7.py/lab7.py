#Daniel Ferreira
import numpy as np

#1)
def senoPositivo(a:int , b:int , n:int):
    c = np.linspace(a , b , n)
    d = np.sin(c) > 0
    return c[d]
    
#2)
def polinomio(vetor, z):
    return sum(np.cumprod(vetor))





    
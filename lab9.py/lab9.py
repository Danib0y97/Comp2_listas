#Daniel Ferreira 

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st


#1)
def alturas(n:np.ndarray)-> np.ndarray:
    """A função pede ao usuário que indique o número de alturas corporais de pessoas, utilizando a distribuição normal, em seguida ele plota o gráfico de histogramas desses dados."""

    numeroBins = 20
    
    x = np.random.randn(n)
    y = st.norm.rvs(loc = 1.7, scale = 0.08, size = n)

    fig, axs = plt.subplots(figsize = (6,6))

    axs.hist(x,bins = numeroBins, facecolor= 'c')

    plt.title('Alturas')
    plt.savefig('alturas.png')
    
    
    return y 

#2)

def pesos(alturas:np.ndarray)-> np.ndarray:
  """O usuário insere um array de alturas e a função, usando a distribuição normal, calcula o seu IMC, plotando um histograma."""

    m = len(alturas)
    imc = st.norm.rvs(loc = 24.5, scale = 4.3,size = m) 
    peso = imc * (alturas**2)

    fig, axs = plt.subplots(figsize = (6,6))

    axs.hist(peso, 20) 
    plt.title('Pesos')
    plt.savefig('pesos.png')

    return pesos

#3)
def regressaoLinear(altura: np.ndarray, peso: np.ndarray)-> np.ndarray:
  """Nessa função, o usuário insere um array de altura e peso, em seguida ele cria um gráfico de Altura vs peso, usando a equação linear padrão."""


    a = st.linregress(altura, peso)[0]
    b = st.linregress(altura, peso)[1]
    y = a*altura + b 

    fig, axs = plt.subplots(figsize = (6,6))

    axs.plot(altura, y, 'g')
    plt.scatter(altura, peso,  facecolor= 'y')

    plt.title('Altura vs. peso')
    plt.savefig('regressao.png')

    return a, b

altura0= st.norm.rvs(loc=1.7,scale=0.08,size=100)
peso0=st.norm.rvs(loc = 24.5, scale = 4.3, size = len(altura0))* altura0**2
 
 
#Daniel Ferreira 
#Questão 1
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st


def alturas(n):

 numeroBins = 20
  
 x = np.linspace(1.55, 1.90, n)
 y = st.norm.rvs(loc = 1.7, scale = 0.08, size = n)

 fig, axs = plt.subplot(figssize = (6,6,))

 axs.hist(x,bins = numeroBins)

 plt.title('Alturas')
 plt.savefig('alturas.png')

 
 #retorno (?)

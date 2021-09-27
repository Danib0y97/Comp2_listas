#Daniel Ferreira 
#Questão 1
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st


##comentar a função, identar
def alturas(n):

 numeroBins = 20
  
 x = np.random.randn(n)
 y = st.norm.rvs(loc = 1.7, scale = 0.08, size = n)

 fig, axs = plt.subplots(figsize = (6,6))

 axs.hist(x,bins = numeroBins, facecolor= 'c')

 plt.title('Alturas')
 plt.savefig('alturas.png')
 
 
 return y 
 
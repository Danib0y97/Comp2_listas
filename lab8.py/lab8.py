#Daniel Ferreira 
#Questão 1
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.legend_handler import HandlerLine2D

def racional(n:np.vectorize ): 
  """Nesta função, iremos escolher os valores os números de 0,1 a 2 com a quantidade que o usuário decidir.Então então um gráfico será desenhado com as funções 1/x e 1/x²."""
  
  x = np.linspace(0.1 ,2 ,n)
  cian = plt.plot(x , 1/x, linewidth = 2.0, color = "c", marker = 's', label = 'y = 1/x' )
  magenta = plt.plot(x , 1/x**2 , linewidth = 2.0, color = "m", marker = 'o', label = 'y = 1/x²' )


  cian = plt.Line2D([], [], color='c', marker='s',markersize=2, label ='y = 1/x ')
  magenta = plt.Line2D([], [], color='m', marker='o',markersize=2, label ='y = 1/x^2 ')

  plt.legend(handler_map={cian: HandlerLine2D(numpoints=4)})


  plt.rcParams['figure.figsize'] = (6,6)
  plt.title('Funções racionais')
  plt.show()


#Questão 2
import matplotlib.pyplot as plt
import numpy as np

def polinomios(grau:int):
 ## ""O usuário informa o grau desejado do polinomio e a função plota os gráficos até o grau desejado""
  
  x = np.linspace(-1, 1, 100)
  y = x ** grau
  fig = plt.figure()
  ax = fig.add_subplot()
  ax.plot(x , y)

  
  
  plt.rcParams['figure.figsize'] = (6,6)
  plt.show()

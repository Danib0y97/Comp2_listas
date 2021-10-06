#Daniel Ferreira 

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
import pandas as pd 

#Questão 1
def suites() -> 'series':
    """Essa função conta a frequencia das suites e retorna o valor em Series. Também, faz um gráfico de pizza mostrando os valores das mesmas."""
 df = pd.read_csv("dados.csv")
 freq = df["suites"].value_counts()
  

 fig, axes = plt.subplots()
 
 axes.axis('equal')
 freq.plot.pie(autopct='%1.1f%%')
  
 plt.show()
 return freq

#Questão 2
def area() -> 'DataFrame':
    """Mostra as áreas dos apartamentos em um histograma e o seu valor de retorno possui as linhas com as maiores áreas de todos os apartamentos."""
 df = pd.read_csv("dados.csv")
 df.groupby("area").mean()
 
 area_max = df[df['area']== df['area'].max()]

 fig, axes = plt.subplots()
 
 df["area"].plot.hist( bins=20, color='g')
 
 plt.show()
 return area_max

 #Questão 3 
def procura(preco, area, condominio) -> 'DataFrame':
    """O usuário insere um valor para o preco, area e condominio. Nisso a função devolve os parametros, o preco menor ou igual do que o preco passado, a área maior ou igual e o condominio menor ou igual, distribuidos na coluna dos bairros. Além disso, ela cria um gráfico de barras mostrando os bairros."""
  df = pd.read_csv("dados.csv")
  
  opcoes = df[(df["preco"] <= preco) & (df["area"] >= area) & (df["condominio"] <= condominio)]
  
  r = opcoes["bairro"].value_counts()

  fig, axes = plt.subplots()
  opcoes["bairro"].value_counts().plot.bar(rot = 0, color='orange')
  
  plt.show()
  return r

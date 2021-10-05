#Daniel Ferreira 

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
import pandas as pd 

#Questão 1
def suites() -> 'series':
    """"""
 df = pd.read_csv("dados.csv")
 freq = df["suites"].value_counts()
  

 fig, axes = plt.subplots()
 
 axes.axis('equal')
 freq.plot.pie(autopct='%1.1f%%')
  
 plt.show()
 return freq

#Questão 2
def area() -> 'DataFrame':
    """"""
 df = pd.read_csv("dados.csv")
 df.groupby("area").mean()
 
 area_max = df[df['area']== df['area'].max()]

 fig, axes = plt.subplots()
 
 df["area"].plot.hist( bins=20, color='g')
 
 plt.show()
 return area_max

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 11:09:26 2020

@author: andresalvarez
"""

#codigo para analizar la estatura de los presidentes de EEUU

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("president_heights.csv")
print(data.head())

height = np.array(data["height(cm)"])
print (height)

print("Media de alturas =", height.mean())
print("Desviacion estandar de la altura =", height.std())
print("Altura minima =", height.min())
print("Altura maxima =", height.max())

print("Percentil 25avo =", np.percentile(height, 25))
print("Media =", np.median(height))
print("Percentil 75avo =", np.percentile(height, 75))

sns.set()

plt.hist(height)
plt.title("Distribucion de la altura de los presidentes de EEUU")
plt.xlabel("Altura(cm)")
plt.ylabel("Numero")
plt.show()
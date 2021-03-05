import matplotlib.pyplot as plt
import geopandas as gpd
import pysal as ps
import random as random
import numpy as np

np.random.seed(19680801)
rutaShp = '../data/data.shp'
mapa = gpd.read_file(rutaShp)
y = np.random.randn(8129)

print(mapa.shape)
print(mapa.head())
print(mapa.info())
mapa.plot(cmap='prism',column=y,facecolor='b',alpha=1)

plt.axis("off")
plt.show()

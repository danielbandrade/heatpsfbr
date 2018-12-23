#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 10:32:37 2018

@author: dbaprof
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Carregando os dados das ESF do brasil
dados_esf = pd.read_csv('acs_equipesnone.csv', sep = ',')
dados_brutos = dados_esf 
dados_brutos = dados_brutos[['equipes']]
# Limpeza dos dados
dados_esf = dados_esf[['equipes','lat','long']]

#Tranformando pandas Series em numpy array
esf_lat = dados_esf['lat'].values
esf_lon = dados_esf['long'].values
c = dados_esf['equipes'].values


#Criando mapa do brasil
map = Basemap(projection='mill', 
              llcrnrlon=-77, 
              llcrnrlat=-45, 
              urcrnrlon=-31, 
              urcrnrlat=10,
              lat_0=-18, 
              lon_0=-60,
              resolution = 'l')

map.drawcoastlines()
map.drawcountries()
map.drawstates()


#cmap1 = LinearSegmentedColormap.from_list("my_colormap", ((0, 0, 0), (1, 1, 1)), N=6, gamma=1.0)

x, y = map(esf_lon,esf_lat)
map.hexbin(x, y, C = c, bins = 20, cmap='tab20c')
plt.colorbar()
#map.colorbar(location='bottom', format='%d',label='Densidade de Agentes de Saúde')

#plt.title('ESF Alvo')
#plt.show()
plt.savefig('ESF_Alvo.png')


#print(dados_esf.head())
#print(type(c))




#if float(info['amplitude']) < 0:
#        c.append(-1 * float(info['amplitude']))
#    else:
#        c.append(float(info['amplitude']))
    



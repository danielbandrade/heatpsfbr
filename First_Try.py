#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 13:08:33 2018

@author: dbaprof
"""
#from shapely.geometry import Point, MultiPoint
import os
os.system('clear')
unused_variable = os.system("clear")
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dados_ubs = pd.read_csv('lista_dados_sage.csv', sep = ';')
#dados_ubs = dados_ubs.reset_index()
dados_ubs = dados_ubs[['cidade','no_fantasia','cnes','lat','long']]
#print(dados_ubs.head())

ubs_lat = dados_ubs['lat'].values
ubs_lon = dados_ubs['long'].values

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

x, y = map(ubs_lon,ubs_lat)
map.plot(x, y,'c^' , markersize=0.5)



plt.title('UBS Alvo')
plt.show()
#plt.savefig('UBS Alvo.png')



import socket
import numpy as np
import listado_codecs as lc

# variables de entranda
enlace = 1
mos = 4
rt = 150
rt_red = 75
rt_jitter = 1.5*(30) # valor del jitter 
Bw = 0
Pb = 0


list_codec = lc.lista_Codecs()
enlaces = ['1','2','3','4','5']

list = []

enlace = enlaces[enlace]

# Coger MOS igual o superior al ofrecido por el cliente
for i in list_codec:
    if i.getMOS() >= mos:
        list.append(i)

print(list)

x = list.copy()
# calcular retardo Paso 3
for i in x:
    ms = i.getVPSs()
    ms += 0.1*(i.getCSI()) + rt_red + (rt_jitter) + (0.1*(i.getCSI())*(i.getVPSs()/i.getCSI()))
    if ms > rt:
        list.remove(i)

print(list)

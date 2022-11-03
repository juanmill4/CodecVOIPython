import socket
import erlang 
import numpy as np
import listado_codecs as lc


# variables de entranda
enlace = 4
mos = 4
rt = 150
rt_red = 75
rt_jitter = 1.5*(30) # valor del jitter 
Bw = 4000000
Bw_res = 1.1
Pb = 0
cRTP = 0
Nc = 150
Nl = 20
tpll = 3
#########

list_codec = lc.lista_Codecs()
enlaces = [18,22,26,26,30]

list = []

enlace = enlaces[enlace]

# Coger MOS igual o superior al ofrecido por el cliente
for i in list_codec:
    if i.getMOS() >= mos:
        list.append(i)

print(list)
if (len(list) == 0):
    print('Coge un MOS inferior porque no cumple ninguno con el retardo')
    exit()

x = list.copy()
# calcular retardo Paso 3
for i in x:
    ms = i.getVPSs()
    ms += 0.1*(i.getCSI()) + rt_red + (rt_jitter) + (0.1*(i.getCSI())*(i.getVPSs()/i.getCSI()))
    if ms > rt:
        list.remove(i)

print(list)
if (len(list) == 0):
    print('Coge un MOS inferior porque no cumple ninguno con el retardo')
    exit()

x = list.copy()
# Calcular Paso 4
#########################################

E = (Nc * Nl * tpll)/60.0
print(E)
nll = erlang.extended_b_lines(E, 0.003)

print(nll) 

########################################

# Calcular Paso 5
x = list.copy()

if cRTP == 1:

    payload = 4
    cabecera = enlace + payload
    print(cabecera)
    for i in x:
        bw = ((cabecera + i.getVPSb())*8) * i.getPPS()
        bw *= nll * Bw_res
        print(bw)
        if bw > Bw:
            list.remove(i) 

else:

    payload = 20 + 8 + 12
    cabecera = enlace + payload
    print(cabecera)
    for i in x:
        bw = ((cabecera + i.getVPSb())*8) * i.getPPS()
        bw *= nll * Bw_res
        print(bw)
        if bw > Bw:
            list.remove(i) 

print(list)
if (len(list) == 0):
    print('Coge un MOS inferior porque no cumple ninguno con el retardo')
    exit()

# PASO 6 ############# Volver a hacer todo lo anterior





# -*- coding: utf-8 -*-
"""
Spyder Editor


"""

n_lineas=0
largo=0
import numpy as np
import matplotlib.pyplot as plt

fileWrite = open('archivocaracteres.out', 'wt')  

with open("datos.txt", 'rt') as file:
    for line in file: 
        if chr(9) in line:
            n_lineas=n_lineas+1
        


m=np.zeros((n_lineas,2))

pos_linea=0
with open("datos.txt", 'rt') as file:
    for line in file:  
        if chr(9) in line:
            x=float(line[:line.find(chr(9))])
            y=float(line[line.find(chr(9)):])
            m[pos_linea][0]=x
            m[pos_linea][1]=y
            #print(x," ",y)
            # fig, grafico = plt.subplots()
            # grafico.scatter(x,y)
            # plt.show()
            #print(line[i], "ordinal:", ord(line[i]))
       
            pos_linea=pos_linea+1
        #print("nueva linea")   


# for i in range (n_lineas):
#     for j in range (1):
#         fig, grafico = plt.subplots()
#         grafico.scatter(m[i][j])
#         plt.show()        


fileWrite.close()











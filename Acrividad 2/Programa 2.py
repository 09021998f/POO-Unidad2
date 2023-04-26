# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 19:52:33 2023

@author: Facu
"""
from claseViajeroFrecuente import ViajeroFrecuente

from claseViajeroFrecuente import Manejador

if __name__ == '__main__':
    
    mv = Manejador()
    mv.testViajero()
    print(mv)
    numV = int(input("Ingrese numero de viajero: "))
    i = mv.buscarViajero(numV)
    if i == None:
        print("Viajero no disponible")
    else:
        print("1-Consultar cantidad de millas\n2-Acumular millas\n3-Cajear millas")
        op=int(input("Opcion:"))
        while(op!=0):
            if  op == 1:
                mile=mv.getOp1(i)
                print('Millas acumuladas: ', mile )
                
            elif op == 2:
                aCanje =int(input("Ingrese Millas recorridas: "))
                print("***Millas actualizadas***")
                print("Millas que tenia antes: ", mv.getMillas(i))
                mile = mv.getOp2(i, aCanje)
                print("Millas actuales: ",(mv.getMillas(i)))
            elif op == 3:
                mCanje = int(input("Ingrese millas a canjear: "))
                print("Millas Anteriores: ", mv.getMillas(i))
                mile =mv.getOp3(i, mCanje)
            print("*"*20)
            op=int(input("Opcion  '0' para salir:"))   
            
            
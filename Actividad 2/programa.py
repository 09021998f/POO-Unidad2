# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 20:28:09 2023

@author: Facu
"""

from claseViajeroFrecuente import ViajeroFrecuente
import csv

def creaLista(lista):
    archivo = open('viajeros.csv')
    reader = csv.reader(archivo,delimiter=";")
    for fila in reader:
        nv, dni, nom, ap, ma = fila
        viajero = ViajeroFrecuente(nv, dni, nom, ap, ma)
        lista.append(viajero)
        
    
def menu(numV, lista):
    print("1-Consultar cantidad de millas")
    print("2-Acumular Millas")
    print("3-Canjear Millas")
    print("0-Salir")
    op = int(input("Opcion: "))
    i=0
    band = True
    if(op == 1):
        while(band | i<len(lista)):
            if(lista[i].getNumViajero() == numV):
                     print(lista[i].cantidadTotalMillas())
                     band = not band
            i = i+1
        if(band == True):
            print("no se encontro el numero")      
        i=0
        band = True
    
    if(op == 2):
        while (band|  i<len(lista)):
            if(lista[i].getNumViajero()==numV):
                millasRecorridas = int(input("Ingrese millas recorridas: "))
                lista[i].acumularMillas(millasRecorridas)
                print("Millas acumuladas actualizado: ", lista[i].cantidadTotalMillas())
                band = not band
                
            i=i+1   
        if(band == True):
            print("no se encontro el numero")
                
        i=0
        band = True
    if(op==3):
       while (band|  i<len(lista)):
           if(lista[i].getNumViajero()==numV):
               millasAcanjear = int(input("Millas a canjear: "))
               lista[i].canjearMillas(millasAcanjear)
               
               band = not band
           i=i+1     
       if(band == True):
            print("no se encontro el numero")
                
       i=0
       band = True
       
        
if __name__ == '__main__':
    
    
    lista = []
    
    creaLista(lista)
    #x =len(lista)
    lista.sort()
    
    lista.sort(key = lambda p: p.getNombre())
    filtra_prod = list(filter(lambda x: x.getNombre() == "Facundo", lista))
    for lista in lista:
        print(lista)
        print("-"*25)
        
    print("Lista filtrada por nombre")
    
    print(filtra_prod)
                
               
      
        
   
   
        
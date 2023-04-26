# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 20:15:57 2023

@author: Facu
"""
import csv
class ViajeroFrecuente:
    __numViajero = 0
    __dni = ''
    __nombre=''
    __apellido=''
    __millasAcumuladas = 0

    def __init__(self, nv,dni,nom,ap,ma):
        self.__numViajero = int(nv)
        self.__dni=dni
        self.__nombre = nom
        self.__apellido = ap
        self.__millasAcumuladas = int(ma)
    
        
    def getNumViajero(self):
        return int(self.__numViajero)
    
    def getNombre(self):
        return self.__nombre
    
    def getTotalMillas(self):
        return self.__millasAcumuladas
    
    def acumularMillas(self, mr):
        self.__millasAcumuladas = self.__millasAcumuladas + mr 
        
        
    def canjearMillas(self,millasACanjear):
        if(millasACanjear < self.__millasAcumuladas):
            print("Millas canjeadas: ", millasACanjear)
            self.__millasAcumuladas = self.__millasAcumuladas - millasACanjear
            print("Millas disponibles: ", self.__millasAcumuladas)
        else:
            print("Cantidad insuficiente Usted tiene ", self.__millasAcumuladas," millas")
            
  
    def __repr__(self):
       
        return f'Numero de Viajero: {self.__numViajero}\nDNI: {self.__dni}\nNombre: {self.__nombre}\nApellido: {self.__apellido}\nMillas Acumuladas: {self.__millasAcumuladas}\n******* '
    
    def __lt__(self, otro):
        return self.__numViajero < otro.__numViajero


class Manejador:
    
    
    def __init__(self):
        self.__lista=[]
        
    def agregarViajero(self , unViajero):
        self.__lista.append(unViajero)
        
    
        
    def testViajero(self):
        archivo = open('viajeros.csv')
        reader = csv.reader(archivo, delimiter = ";")
        for fila in reader:
                nv = int(fila[0])
                dni = int(fila[1])
                nom = fila[2]
                ap = fila[3]
                ma = fila[4]
                unViajero = ViajeroFrecuente(nv, dni, nom, ap, ma)
                self.agregarViajero(unViajero)
     
        archivo.close()
                
    def buscarViajero(self, num):
        i = 0
        vRet= None
        band = True
        while band  and i < len(self.__lista):
            
            if self.__lista[i].getNumViajero()==num:
                band == False
                
                vRet = i
                break;
            else:
                i= i+1
        print(vRet)
        return vRet
    
    
    def __str__(self):
         
        s = " "
        for fila in self.__lista:
            s += str(fila) + '\n'
        
        return s
    
    def getOp1(self, i):
        return self.__lista[i].getTotalMillas()
    
    def getOp2(self, i, aCanje):
        return self.__lista[i].acumularMillas(aCanje)

    def getOp3(self, i, mCanje):
        return self.__lista[i].canjearMillas(mCanje)
    
    def getMillas(self , i):
        return self.__lista[i].getTotalMillas()
        

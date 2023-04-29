# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:45:24 2023

@author: Facu
"""
import csv

class Registro:
    __dia=0
    __hora=0
    __varTemp=0
    __varHum=0
    __varPsAtm=0
    
    def __init__(self,temp,hum,psatm,dia,hora):
        self.__varTemp = temp
        self.__varHum = hum
        self.__varPsAtm = psatm
        self.__dia = dia
        self.__hora = hora

    def __repr__(self):
        return f'| Dia | Hora |Temperatura| Humedad | Presion Atm |\n    {self.__dia}     {self.__hora}     {self.__varTemp}     {self.__varHum}         {self.__varPsAtm}' 

        
class Manejador:
    def __init__(self,):
       self.__regMet = [[] for _ in range(2)]


    def addReg(self, reg, dia):
       self.__regMet[dia-1].append(reg)

    def testRegMet(self):
        archi = open('registro.csv')
        reader = csv.reader(archi, delimiter=";")

        for fila in reader:
            dia = int(fila[0]) 
            hora = int(fila[1])
            temp = float(fila[2])      
            humedad = float(fila[3])
            presion = float(fila[4])
            reg = Registro(temp, humedad, presion, dia, hora)
            self.addReg(reg, dia)
        archi.close()
        
        
    def __str__(self):
         
        s = " "
        for dia in range(len(self.__regMet)):
            for fila in self.__regMet[dia]:
                s += str(fila) + '\n'
        return s
        

    
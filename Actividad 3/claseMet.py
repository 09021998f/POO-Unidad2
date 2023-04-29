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

    def getTemp(self):
        return self.__varTemp
    
    def getHumedad(self):
        return self.__varHum
    
    def getPresion(self):
        return self.__varPsAtm
    
    def getHora(self):
        return self.__hora

    def __lt__(self, otro):
        return self.__varTemp < self.__varTemp
    
        
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
    #Temperatura 
    def getMaximoTemp(self):
        max = 0
        hora = 0
        for dia in range(len(self.__regMet)):
            for i in range(len(self.__regMet[dia])):
                if(self.__regMet[int(dia)][i].getTemp() > max):
                    max = self.__regMet[int(dia)][i].getTemp()
                    hora = self.__regMet[int(dia)][i].getHora()
            print(f'Temperatura maxima del dia {dia+1}: {max}°C a las {hora}:00')
            max = 0
        
    def getMinimoTemp(self):
        min = 9999999
        hora = 0
        for dia in range(len(self.__regMet)):
            for i in range(len(self.__regMet[dia])):
                if(self.__regMet[int(dia)][i].getTemp() < min):
                    min = self.__regMet[int(dia)][i].getTemp()
                    hora = self.__regMet[int(dia)][i].getHora()
            print(f'Temperatura minima del dia {dia+1}: {min}°C a las {hora}:00')
            min = 999999
    #Huemedad
    def getMaximoHumedad(self):
        max = 0
        hora = 0
        for dia in range(len(self.__regMet)):
            for i in range(len(self.__regMet[dia])):
                if(self.__regMet[int(dia)][i].getHumedad() > max):
                    max = self.__regMet[int(dia)][i].getHumedad()
                    hora = self.__regMet[int(dia)][i].getHora()
            print(f'Humedad maxima del dia {dia+1}: {max} a las {hora}:00')
            max = 0

    def getMinimoHumedad(self):
        min = 9999999
        hora = 0
        for dia in range(len(self.__regMet)):
            for i in range(len(self.__regMet[dia])):
                if(self.__regMet[int(dia)][i].getHumedad() < min):
                    min = self.__regMet[int(dia)][i].getHumedad()
                    hora = self.__regMet[int(dia)][i].getHora()
            print(f'Humedad minimaa del dia {dia+1}: {min} a las {hora}:00')
            min = 999999

    #Presion atmosferica
    def getMaximoPresion(self):
        max = 0
        hora = 0
        for dia in range(len(self.__regMet)):
            for i in range(len(self.__regMet[dia])):
                if(self.__regMet[int(dia)][i].getPresion() > max):
                    max = self.__regMet[int(dia)][i].getPresion()
                    hora = self.__regMet[int(dia)][i].getHora()
            print(f'Presion Atmoesferica maxima del dia {dia+1}: {max}atm a las {hora}:00')
            max = 0

    def getMinimoPresion(self):
        min = 9999999
        hora = 0
        for dia in range(len(self.__regMet)):
            for i in range(len(self.__regMet[dia])):
                if(self.__regMet[int(dia)][i].getPresion() < min):
                    min = self.__regMet[int(dia)][i].getPresion()
                    hora = self.__regMet[int(dia)][i].getHora()
            print(f'Presion Atmosferica minimaa del dia {dia+1}: {min}atm a las {hora}:00')
            min = 999999

    def menu(self):
        print("1- Mostrar punto 1")
        print("0-Salir")
        print()
        op = int(input("Opcion: "))

        if(op==1):
            print("*"*30)
            self.getMaximoTemp()
            print("*"*30)
            self.getMinimoTemp()
            
            print("*"*30)
            self.getMaximoHumedad()
            print("*"*30)
            self.getMinimoHumedad()
            
            print("*"*30)
            self.getMaximoPresion()
            print("*"*30)
            self.getMinimoPresion()
             


    
    
    
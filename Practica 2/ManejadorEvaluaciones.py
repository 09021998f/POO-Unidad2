from clasePuntaje import Puntaje
from ManejadorFederados import ManejadorFed

import csv
class ManejadorEv:

    def __init__(self) -> None:
        self.__listaEv=[]
        self.__ManejadorFed = ManejadorFed()

    def testEv(self):
        archi = open('evaluacion.csv', encoding='utf-8-sig')
        reader = csv.reader(archi, delimiter=";")
        for i in reader:
            ev = Puntaje(int(i[0]),i[1],float(i[2].replace(",", ".")), float(i[3].replace(",", ".")), float(i[4].replace(",", ".")))
            self.__listaEv.append(ev)

    def __str__(self):
        s=""
        for fila in self.__listaEv:
            s += str(fila) + '\n'
        return s
    

    def puntoA(self,est):
        self.__ManejadorFed.testFed()
        for i in range(len(self.__listaEv)):
            if(self.__listaEv[i].getEstilo() == est.upper()):
                
                dni = self.__listaEv[i].getDni()
                self.__ManejadorFed.puntoA1(dni)
            
    def puntoB(self):
        prom = 0.0
        self.__ManejadorFed.testFed()
        for i in range(len(self.__listaEv)):
            if self.__listaEv[i].getPromedio() > prom:
                dni =  self.__listaEv[i].getDni()
                prom = self.__listaEv[i].getPromedio()
                est = self.__listaEv[i].getEstilo()
        
        self.__ManejadorFed.puntoB1(dni,est)
        
    def puntoC(self):
        self.__ManejadorFed.testFed()
        dni2=0
        for i in range(len(self.__listaEv)):
            dni = self.__listaEv[i].getDni()
            if(self.__listaEv[i].getEstilo() == "L" ):
                for j in range(len(self.__listaEv)):                    
                    if(self.__listaEv[j].getEstilo() == "E" and dni == self.__listaEv[j].getDni() ):
                        dni2 = self.__listaEv[j].getDni()
                        self.__ManejadorFed.puntoC1(dni2)

    def puntoD(self,dni,est):
        self.__ManejadorFed.testFed()

        for i in range(len(self.__listaEv)):
            if self.__listaEv[i].getDni() == dni and self.__listaEv[i].getEstilo() == est:
                print(f'Puntaje 1:{self.__listaEv[i].getP1()} Puntaje 2:{self.__listaEv[i].getP2()} Puntaje 3:{self.__listaEv[i].getP3()}')
        

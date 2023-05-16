from claseFederados import Federado


import csv
class ManejadorFed:
    def __init__(self):
        self.__listaFed = []
        


    def testFed(self):
        archi = open('federados.csv', encoding='utf-8-sig')
        reader = csv.reader(archi, delimiter= ";")
        for i in reader:
            fed = Federado(i[0],i[1],int(i[2]),i[3],i[4])
            self.__listaFed.append(fed)
        archi.close()

    def mostrarDatos(self):
        for i in range(len(self.__listaFed)):
            print(self.__listaFed[i].getNom())

    def puntoA1(self, dni):
        i = 0
        band = True
        while band and i < len(self.__listaFed):
            
            if(self.__listaFed[i].getDni() == dni):
                
                print(f'Apellido :{self.__listaFed[i].getAp()} Nombre:{self.__listaFed[i].getNom()} Dni:{dni}')
                band = False
            else:
                i+=1

    def puntoB1(self,dni,est):
        i = 0
        band = True
        while band and i  < len(self.__listaFed):
            if (self.__listaFed[i].getDni() == dni):
                print(f'Apellido :{self.__listaFed[i].getAp()} Nombre:{self.__listaFed[i].getNom()} Etilo:{est} Club:{self.__listaFed[i].getClub()}')
                band = False
            else:
                i+=1

    def puntoC1(self,dni):
        i=0
        band = True
        
        while band and i<len(self.__listaFed):
            if(self.__listaFed[i].getDni() == dni):
                print(f'Nombre Y apellido :{self.__listaFed[i].getNom()} {self.__listaFed[i].getAp()} Dni:{self.__listaFed[i].getDni()} Edad:{self.__listaFed[i].getEdad()}')
                print(f'Club:{self.__listaFed[i].getClub()}')
                
                band = False
            else:
                i+=1
            
from claseReparacion import Reparacion
import csv
class ManejadorRep:
    def __init__(self) -> None:
        self.__listaRep = []

    def testRep(self):
        archi = open('reparaciones.csv')
        reader = csv.reader(archi,delimiter=";")
        next(reader)
        for i in reader:
            r = Reparacion(i[0],i[1],int(i[2]),int(i[3]),i[4])
            self.__listaRep.append(r)
        archi.close()

    def puntoA1(self,pat):
        pRep = 0
        pMano = 0
        band = False
        for i in range(len(self.__listaRep)):
            if(self.__listaRep[i].getPatente() == pat):
                band = True
                pRep = pRep + self.__listaRep[i].getPrecioRep()
                pMano = pMano + self.__listaRep[i].getPrecioMano()
                print("------------------------------------------------")
                print(f"Reparacion:{self.__listaRep[i].getReparacion()} ")
                print(f'Precio de Repuesto:{self.__listaRep[i].getPrecioRep()}$')
                print(f"Precio de mano de obra: {self.__listaRep[i].getPrecioMano()}$")
            
                
        if(band == True):
            print(f"Subtotal Repuestos: {pRep}$")
            print(f"Subtotal Mano de obra:{pMano}$")        
            print(f"Total:", pRep + pMano,"$")    
            print("------------------------------------------------")
        else:
            print("No se encontro DNI")

    def puntoB1(self,pat):
        lista = []
        pRep=0
        pMano=0
        for i in range(len(self.__listaRep)):
            if(self.__listaRep[i].getPatente() == pat):
                lista.append(self.__listaRep[i].getEstado())
        if (all(elem == lista[0] for elem in lista)):
            for i in range(len(self.__listaRep)):
                if(self.__listaRep[i].getPatente() == pat):
                    pRep = pRep + self.__listaRep[i].getPrecioRep()
                    pMano = pMano + self.__listaRep[i].getPrecioMano()
        print("Total a pagar:", pRep + pMano,"$")
                
    def puntoC1(self,pat):
        i=0
        band = True
        while band and i < len(self.__listaRep) :
            if(self.__listaRep[i].getPatente() == pat):
                print(f"Reparacion:{self.__listaRep[i].getReparacion()} ")
                print("-------------------------------------------------")
                band = False
            else:
                i+=1
    

        
    

    

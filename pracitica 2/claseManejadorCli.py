from claseCliente import Cliente
from claseManejadorRep import ManejadorRep
import csv

class ManejadorCli:
    def __init__(self):
        self.__listaCli = []
        self.__manejadorRep = ManejadorRep()

    def testCliente(self):
        archi = open('clientes.csv')
        reader = csv.reader(archi,delimiter=";")
        next(reader)
        for i in reader:
            c = Cliente(int(i[0]),i[1],i[2],i[3],i[4],i[5],i[6])
            self.__listaCli.append(c)
        archi.close()
    
    def __str__(self):
        s = " "
        for fila in self.__listaCli:
            s += str(fila) + "\n"
        return s

    def puntoA(self,dni):
        self.__manejadorRep.testRep()
        for i in range(len(self.__listaCli)):
            if(self.__listaCli[i].getDni() == dni):
                pat = self.__listaCli[i].getPatente()
                print(f"Apellido y Nombre: {self.__listaCli[i].getAp()} {self.__listaCli[i].getNombre()}")
                print(f"DNI:{self.__listaCli[i].getDni()} Patente:{self.__listaCli[i].getPatente()} Vehiculo:{self.__listaCli[i].getVehiculo()}")
                self.__manejadorRep.puntoA1(pat)

    def puntoB(self, pat):
        self.__manejadorRep.testRep()
        i=0
        band = True
        while band and i < len(self.__listaCli):
            if(self.__listaCli[i].getPatente() == pat):
                band = False
                print(f"Apellido y Nombre: {self.__listaCli[i].getAp()} {self.__listaCli[i].getNombre()}")
                print(f"DNI:{self.__listaCli[i].getDni()} Patente:{self.__listaCli[i].getPatente()} Vehiculo:{self.__listaCli[i].getVehiculo()}")
                
                self.__manejadorRep.puntoB1(pat)

            else:
                i+=1
        if(band):
            print("Patente no encontrada")
        
    def puntoC(self):
        self.__manejadorRep.testRep()
        for i in range(len(self.__listaCli)):
            
            if(self.__listaCli[i].getEstado() == 'P'):            
                print(f"| Apellido y Nombre: {self.__listaCli[i].getAp()} {self.__listaCli[i].getNombre()} Telefono")
                print(f"DNI:{self.__listaCli[i].getDni()} | Patente:{self.__listaCli[i].getPatente()} Vehiculo:{self.__listaCli[i].getVehiculo()}")    
                pat = self.__listaCli[i].getPatente()
                self.__manejadorRep.puntoC1(pat.upper())
    
    def puntoD(self):
        iguales = []
        for i in range(len(self.__listaCli)):
            
            for j in range(i + 1, len(self.__listaCli)):
                if self.__listaCli[i] == self.__listaCli[j]:
                    iguales.append([i,j])
        
        for i in range(len(iguales[0])):
            j = iguales[0][i]
            print(self.__listaCli[j])
import csv
class Plan:

    __codPlan=0
    __modelo = ""
    __version= ""
    __valorCar = 0
    __cantCuotas = 0
    __cantCuotAcre= 0

    def __init__(self, cod, mod, ver, valorCar, cantC, cantCA):
        self.__codPlan = cod
        self.__modelo = mod
        self.__version = ver
        self.__valorCar = valorCar
        self.__cantCuotas = cantC
        self.__cantCuotasAcre = cantCA

    def __repr__(self):
        return f'Codigo del plan: {self.__codPlan}\nModelo: {self.__modelo}\nVersion: {self.__version}\nValor del auto: {self.__valorCar}\n**********'

class ManejadorPlan:
    
    def __init__(self):
        self.__lista = []

    def agregarAuto(self, auto):
        self.__lista.append(auto)

    def testPlanes(self):
        with open('planes.csv', 'r') as archi:
            reader = csv.reader(archi, delimiter=";")
            for fila in reader:
                cod = fila[0]
                mod = fila[1]
                ver = fila[2]
                valorCar = fila[3]
                cantC = fila[4]
                cantCA = fila[5]
                auto = Plan(cod, mod, ver, valorCar, cantC, cantCA)
                self.agregarAuto(auto)
     
    def __str__(self):
        s = " "
        for fila in self.__lista:
            s += str(fila) + '\n'
        return s
    
     
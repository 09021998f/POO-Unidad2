import csv
class Plan:

    __codPlan=0
    __modelo = ""
    __version= ""
    __valorCar = 0
    __cantCuotas = 0
    __cantCuotasAcre= 0

    def __init__(self, cod, mod, ver, valorCar, cantC, cantCA):
        self.__codPlan = cod
        self.__modelo = mod
        self.__version = ver
        self.__valorCar = valorCar
        self.__cantCuotas = cantC
        self.__cantCuotasAcre = cantCA


    def __repr__(self):
        return f'Codigo del plan: {self.__codPlan}\nModelo: {self.__modelo}\nVersion: {self.__version}\nValor del auto: {self.__valorCar}\n**********'

    def getCodPlan(self):
        return self.__codPlan
    
    def getModelo(self):
        return self.__modelo
    
    def getVersion(self):
        return self.__version
    
    def getValor(self):
        return self.__valorCar

    def getCuotasAcred(self):
        return self.__cantCuotasAcre
    
    def actualizaValor(self, valorNuevo):
        self.__valorCar = valorNuevo

    def modificaCuotasAcred(self, cant):
        self.__cantCuotasAcre = cant

    def getValorCuotas(self):
        return (self.__valorCar / self.__cantCuotas) + self.__valorCar *0.10
    

class ManejadorPlan:
    
    def __init__(self):
        self.__lista = []

    def agregarAuto(self, auto):
        self.__lista.append(auto)

    def testPlanes(self):
        with open('planes.csv', 'r') as archi:
            reader = csv.reader(archi, delimiter=";")
            for fila in reader:
                cod = int(fila[0])
                mod = fila[1]
                ver = fila[2]
                valorCar = float(fila[3])
                cantC = int(fila[4])
                cantCA = int(fila[5])
                auto = Plan(cod, mod, ver, valorCar, cantC, cantCA)
                self.agregarAuto(auto)
     
    def __str__(self):
        s = " "
        for fila in self.__lista:
            s += str(fila) + '\n'
        return s
    
    def actValorCar(self):
        band = True
        i=0
        while i < len(self.__lista):
            print("-"*30)
            print("Codigo: ",self.__lista[i].getCodPlan())
            print("Modelo: ",self.__lista[i].getModelo())
            print("Version: ",self.__lista[i].getVersion())
            print("-"*30)
            valorNuevo = float(input("Ingrese valor actualizado del auto: "))
            print("Precio anterior:", self.__lista[i].getValor())
            self.__lista[i].actualizaValor(valorNuevo)
            print("Precio actualizado:", self.__lista[i].getValor())
            i += 1
    
    def op2(self):
        i=0
        valor = float(input("Ingrese valor: "))
        while i < len(self.__lista):
            if(self.__lista[i].getValorCuotas() < valor ):
                print("-"*30)
                print("Codigo: ",self.__lista[i].getCodPlan())
                print("Modelo: ",self.__lista[i].getModelo())
                print("Version: ",self.__lista[i].getVersion())
                print("Valor de la cuota:",round(self.__lista[i].getValorCuotas(), 2) )
                print("-"*30)
            i+=1

    def op3(self):
        for i in range(len(self.__lista)):
            print("-"*30)
            print("Codigo: ",self.__lista[i].getCodPlan())
            print("Modelo: ",self.__lista[i].getModelo())
            print("Version: ",self.__lista[i].getVersion())
            print("Valor de la cuota:",round(self.__lista[i].getValorCuotas(), 2) )
            print("-"*30)
            monto = self.__lista[i].getValorCuotas() * self.__lista[i].getCuotasAcred()
            print("Monto para licitar el vehiculo:", round(monto, 2))

    def op4(self):
        cod= int(input("Codigo del plan: "))
        i=0
        band = True
        while band and i<len(self.__lista):
            
            if(self.__lista[i].getCodPlan() == cod):
                x = int(input("Cantidad de cuotas: "))
                print("Cuotas anteriores:", self.__lista[i].getCuotasAcred())
                self.__lista[i].modificaCuotasAcred(x)
                print("Cantidad de cuotas actualizada a:", self.__lista[i].getCuotasAcred())
                band = not band
            else:
                i+=1




    def menu(self):
        print("1- Punto a")
        print("2- Punto b")
        print("3- Punto c")
        print("4- Punto d")
        print("0- Salir")
        op = int(input("Opcion: "))

        if(op==1):
            self.actValorCar()
        elif(op==2):
            self.op2()
        elif(op == 3):
            self.op3()
        elif(op==4):
            self.op4()
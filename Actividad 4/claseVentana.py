class Ventana:
    __titulo = ""
    __xVerInf = 0
    __yVerInf = 0
    __xVerSup = 0
    __yVerSup = 0

    def __init__(self, tit, xvs = 0, yvs = 0, xvi = 500, yvi = 500 ):
        self.__xVerInf = xvi
        self.__xVerSup = xvs
        self.__yVerInf = yvi
        self.__yVerSup = yvs
        self.__titulo = tit

    def mostrar(self):
        print("Titulo: ", self.__titulo)
        print("X del vertice inferior izquierdo:", self.__xVerInf)
        print("Y del vertive inferior izquierdo:", self.__yVerInf)
        print("X del vertice superior derecho:", self.__xVerSup)
        print("Y del vertice superior derecho:", self.__yVerSup)

    def getTitulo(self):
        return self.__titulo
    
    def ancho(self):
        return self.__xVerInf - self.__xVerSup
    
    def alto(self):
        return self.__yVerInf - self.__yVerSup
    
    def moverDerecha(self, x):
        self.__xVerSup = self.__xVerSup + x

    def moverIzquierda(self, x):
        self.__xVerSup = self.__xVerSup - x

    def bajar(self, y=0):
        self.__yVerInf = self.__yVerInf - y

    def subir(self, y=0):
        self.__yVerSup = self.__yVerSup - y
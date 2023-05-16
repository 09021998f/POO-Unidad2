class Puntaje:
    
    def __init__(self,dni,est,p1,p2,p3):
        self.__dni = dni
        self.__estilo= est
        self.__puntaje1 = p1
        self.__puntaje2 = p2
        self.__puntaje3 = p3

    def getDni(self):
        return self.__dni
    
    def getEstilo(self):
        return self.__estilo
    
    def getP1(self):
        return self.__puntaje1
    
    def getP2(self):
        return self.__puntaje2
    
    def getP3(self):
        return self.__puntaje3
    
    def getPromedio(self):
        prom = (self.__puntaje1 + self.__puntaje2 + self.__puntaje3) / 3
        return prom
    
    def __gt__(self, otro):
        return self.getPromedio() > otro.getPromedio()
    
    def __repr__(self):
        return f'dni{self.__dni} estilo {self.__estilo}'

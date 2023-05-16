class Reparacion:
    def __init__(self,pat,rep,pRepu,pMano,est):
        self.__patente = pat
        self.__reparacion = rep
        self.__pRepuesto = pRepu
        self.__pManoObra = pMano
        self.__estado = est

    def getPatente(self):
        return self.__patente
    def getReparacion(self):
        return self.__reparacion
    def getPrecioRep(self):
        return self.__pRepuesto
    def getPrecioMano(self):
        return self.__pManoObra
    def getEstado(self):
        return self.__estado
class Federado:

    def __init__(self, ap,nom,dni,edad,club):
        self.__apellido = ap
        self.__nombre = nom
        self.__dni = dni
        self.__edad = edad
        self.__club = club


    def getAp(self):
        return self.__apellido
    def getNom(self):
        return self.__nombre
    def getDni(self):
        return self.__dni
    def getClub(self):
        return self.__club
    def getEdad(self):
        return self.__edad
    
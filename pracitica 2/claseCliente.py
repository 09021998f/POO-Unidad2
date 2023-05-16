class Cliente:
    def __init__(self, dni,ap,nom,tel,pat,veh,est):
        self.__dni = dni
        self.__apellido = ap
        self.__nombre = nom 
        self.__telefono = tel
        self.__patetente = pat
        self.__vehiculo = veh
        self.__estado = est

    def getDni(self):
        return self.__dni
    def getAp(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre
    def getTelefono(self):
        return self.__telefono
    def getPatente(self):
        return self.__patetente
    def getVehiculo(self):
        return self.__vehiculo
    def getEstado(self):
        return self.__estado

    def __repr__(self):
        return f'| Nombre Y Apellido:{self.__nombre} {self.__apellido} | Dni:{self.__dni} | Telefono:{self.__telefono} | Patente:{self.__patetente} | Vehiculo:{self.__vehiculo} '
        
    def __eq__(self, otro):
        return self.__apellido == otro.__apellido and self.__dni == otro.__dni and self.__nombre == otro.__nombre and self.__telefono == otro.__telefono
class ViajeroFrecuente:
    __numViajero = 0
    __dni = ''
    __nombre=''
    __apellido=''
    __millasAcumuladas = 0

    def __init__(self, nv,dni,nom,ap,ma):
        self.__numViajero = int(nv)
        self.__dni=dni
        self.__nombre = nom
        self.__apellido = ap
        self.__millasAcumuladas = int(ma)
    
        
    def getNumViajero(self):
        return int(self.__numViajero)
    
    def getNombre(self):
        return self.__nombre
    
    def getTotalMillas(self):
        return self.__millasAcumuladas
    
    def acumularMillas(self, mr):
        self.__millasAcumuladas = self.__millasAcumuladas + mr 
        
        
    def canjearMillas(self,millasACanjear):
        if(millasACanjear < self.__millasAcumuladas):
            print("Millas canjeadas: ", millasACanjear)
            self.__millasAcumuladas = self.__millasAcumuladas - millasACanjear
            print("Millas disponibles: ", self.__millasAcumuladas)
        else:
            print("Cantidad insuficiente Usted tiene ", self.__millasAcumuladas," millas")
            
  
    def __repr__(self):
       
        return f'Numero de Viajero: {self.__numViajero}\nDNI: {self.__dni}\nNombre: {self.__nombre}\nApellido: {self.__apellido}\nMillas Acumuladas: {self.__millasAcumuladas}\n'
    
    def __gt__(self, otro):
        return self.__millasAcumuladas > otro.__millasAcumuladas

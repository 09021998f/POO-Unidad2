import csv
class Materias:
    __dni= 0
    __materia= ""
    __fecha= ""
    __nota = 0
    __aprobacion = ""

    def __init__(self, dni,mat,fecha,nota,aprob):
        self.__dni = dni
        self.__materia = mat
        self.__fecha = fecha
        self.__nota = nota
        self.__aprobacion= aprob

    def __repr__(self):
        return f'Dni : {self.__dni}|Materia: {self.__materia}|Fecha: {self.__fecha}|Nota: {self.__nota}|Aprobado: {self.__aprobacion}'

    def getNota(self):
        return self.__nota
    
    def getDni(self):
        return self.__dni
    
    def getMat(self):
        return self.__materia
    
    def getAprob(self):
        return self.__aprobacion
    
    def getFecha(self):
        return self.__fecha
        

class ManejadorMaterias:
    def __init__(self):
        self.__lista = []

    def agregarMat(self,materia):
        self.__lista.append(materia)

    def testMaterias(self):
        archi = open('materiasAprobadas.csv')
        reader = csv.reader(archi, delimiter=";")
        next(reader)
        for fila in reader:
            dni = int(fila[0])
            mat = fila[1]
            fecha = fila[2]
            nota = int(fila[3])
            aprob = fila[4]
            materia = Materias(dni,mat,fecha,nota,aprob)
            self.agregarMat(materia)
        archi.close()

    def __str__(self):
        s = " "
        for fila in self.__lista:
            s += str(fila) + '\n'
        return s
    
    def getPromedio(self, dni):
        acum = 0
        cont = 0
        for i in range(len(self.__lista)):
            
            if(dni == self.__lista[i].getDni()):
                acum =  acum +self.__lista[i].getNota()
                cont+=1
                i+=1
            else:
                i+=1
        if(acum != 0):
            prom = acum / cont
            return prom
        
        
    
    def getInfo(self, mat):
        materia = [None]
        for i in range(len(self.__lista)):
            if(mat == self.__lista[i].getMat().lower() and self.__lista[i].getAprob() == "P" ):
                if materia[0] == None:
                    materia = []
                
                materia.append([self.__lista[i].getDni(),self.__lista[i].getMat(),self.__lista[i].getFecha()])
                
                i+=1
            else:
                i+=1
        
        return materia
                

import numpy as np
import csv
    

class Alumno:
    __dni=0
    __apellido = ""
    __nombre = ""
    __carrera = ""
    __añoQueCursa= ""

    def __init__(self, dni, ap, nom, carrera, año):
        self.__dni=dni
        self.__apellido= ap
        self.__nombre = nom
        self.__carrera = carrera
        self.__añoQueCursa = año

    def getDni(self):
        return self.__dni
    
    def getApellido(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre
    
    def getCarrera(self):
        return self.__carrera
    
    def getAño(self):
        return self.__añoQueCursa


class ManejadorAlumnos: 
    
    def __init__(self):
        self.__arreglo = np.empty(8,dtype=Alumno)

    def agregaAlumnos(self):
        pass

    def testAlumnos(self):
        archi = open('alumnos.csv')
        reader = csv.reader(archi, delimiter=";")
        next(reader)
        i=0
        for fila in reader:
            alumno = Alumno(int(fila[0]), fila[1], fila[2], fila[3], fila[4])
            self.__arreglo[i] = alumno
            i=i+1
            if i == 8:
                break;

    def mostrarDatos(self):
    # Imprimimos los datos de los alumnos
        for alumno in self.__arreglo:
            print(f"DNI: {alumno._Alumno__dni} | Apellido: {alumno._Alumno__apellido} | Nombre: {alumno._Alumno__nombre} | Carrera: {alumno._Alumno__carrera} | Año que cursa: {alumno._Alumno__añoQueCursa}")

class Materias:
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
        
        prom = acum / cont
        return prom
    
    def getInfo(self, mat):
        for i in range(len(self.__lista)):
            if(mat == self.__lista[i].get == "P"):
            
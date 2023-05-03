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

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
    
    def __repr__(self):
        return f'Nombre:{self.__nombre} Apellido:{self.__apellido} Año:{self.__añoQueCursa}'
    
    def __lt__(self, otro):
        if self.__añoQueCursa < otro.__añoQueCursa:
            return True
        elif self.__añoQueCursa == otro.__añoQueCursa:
            if self.__nombre < otro.__nombre:
                return True
            elif self.__nombre == otro.__nombre:
                if self.__apellido < otro.__apellido:
                    return True
        return False

   # def __lt__(self, otroAlumno):
   #     if self.__añoQueCursa == otroAlumno.__añoQueCursa:
   #         if self.__nombre == otroAlumno.__nombre:
   #             return self.__nombre < otroAlumno.__nombre
   #         return self.__añoQueCursa < otroAlumno.__añoQueCursa
    
        
    
    


class ManejadorAlumnos: 
    
    def __init__(self):
        self.__arreglo = np.empty(8,dtype=Alumno)

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
    
        for alumno in self.__arreglo:
            print(f"DNI: {alumno._Alumno__dni} | Apellido: {alumno._Alumno__apellido} | Nombre: {alumno._Alumno__nombre} | Carrera: {alumno._Alumno__carrera} | Año que cursa: {alumno._Alumno__añoQueCursa}")
    
    def __str__(self):
        s = " "
        for fila in self.__arreglo:
            s += str(fila) + '\n'
        return s
    
    def getInfo(self,dni):
        band = True
        i=0
        j=0
        datosAlumnos=[]
        for j in range(len(dni)):
            while band and i < len(self.__arreglo):
                if(self.__arreglo[i]._Alumno__dni == dni[j]):
                    datosAlumnos.append([self.__arreglo[i]._Alumno__apellido,self.__arreglo[i]._Alumno__nombre,self.__arreglo[i]._Alumno__añoQueCursa])
                    band = False
                else:
                    i=i+1
            band = True
            i=0
        
        return datosAlumnos
    
    def ordenarPorApellido(self):
        self.__arreglo = np.sort(self.__arreglo)
    
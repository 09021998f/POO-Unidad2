from claseAlumnos import ManejadorAlumnos
from claseMaterias import ManejadorMaterias
import numpy as np



if __name__ == '__main__':

    ma = ManejadorAlumnos()
    ma.testAlumnos()

    mm = ManejadorMaterias()
    mm.testMaterias()



    print("1-Informar promedios")
    print("2-Estudiantes que aprobaron por materia")
    print("3-Listado de alumnos ordenado por año que cursa y alfabeticamente")
    print("0-Salir")
 
    op = int(input("Opcion:"))
    
    while op != 0 :  
        if(op==1):
            dni = int(input("DNI:"))
            if(mm.getPromedio(dni)==None):
                print("Dni no encontrado")
            else:
                print(f'Promedio: {mm.getPromedio(dni)}')
        
        elif(op==2):
            dniDeAprobados= []
            listaConAprobados = []
            mat = input("Materia: ")
            materias = mm.getInfo(mat.lower())
            if(materias[0] == None):
                print("Materia no encontrada")
            else:

                for i in range(len(materias)):
                    dniDeAprobados.append(materias[i][0])
                
                infoAlum = ma.getInfo(dniDeAprobados)
                
                
                for i in range(len(materias)):
                    dni = materias[i][0]
                    materia = materias[i][1]
                    fecha = materias[i][2]
                    for j in range(len(dniDeAprobados)):
                        apellido = infoAlum[j][0]
                        nombre = infoAlum[j][1]
                        año = infoAlum[j][2]
                        if dni == materias[0][0]:
                            break    
                    listaConAprobados.append([dni, apellido, nombre, materia, fecha, año])
                
                        
                print("   DNI  |  Nombre y Apellido   |     Materia      |   Fecha   | Año que cursa")
                for i in range(len(listaConAprobados)):
                    print(f'{listaConAprobados[i][0]}   {listaConAprobados[i][1]}, {listaConAprobados[i][2]}     {listaConAprobados[i][3]}    {listaConAprobados[i][4]}    {listaConAprobados[i][5]}')          

        elif(op==3):
            ma.ordenarPorApellido()
            print(ma)
        print("//*************//")        
        print("1-Informar promedios")
        print("2-Estudiantes que aprobaron por materia")
        print("3-Listado de alumnos ordenado por año que cursa y alfabeticamente")
        print("0-Salir")
        print("//*************//")

        op = int(input("Opcion:"))

    print("//****Programa Terminado****//")
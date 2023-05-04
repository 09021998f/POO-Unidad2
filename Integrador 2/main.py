from claseSIU import ManejadorAlumnos, ManejadorMaterias
if __name__ == '__main__':

    ma = ManejadorAlumnos()     
    ma.testAlumnos()
    ma.mostrarDatos()
    mm = ManejadorMaterias()
    mm.testMaterias()
    print(mm)

    print("1-Informar promedios")
    op = int(input("Opcion:"))

    if(op==1):
        
        dni = int(input("DNI:"))
        print(f'Promedio: {mm.getPromedio(dni)}')
    elif op == 2:
        alumnosAprobados=[]
        dniAprobados = []
        mat = input("Ingrese materia: ")
        materias = mm.getInfo(mat.lower())
        for i in range(len(materias)):
            dniAprobados.append(materias[i][0])
        infoAlum = ma.getInfo(dniAprobados)
        print(infoAlum)
        print(materias)
        
        
        
        
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
        mat = input("Ingrese materia: ")
        materias = mm.getInfo(mat.lower())
        """
         Hecho hasta aca
         materias guarda los datos obtenitos de mm.getInfo() seguir viendo
         como usar materias para obtener los datos del arreglo numpy de alumnos
         """
        
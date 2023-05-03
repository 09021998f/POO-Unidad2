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
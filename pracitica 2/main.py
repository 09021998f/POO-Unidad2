from claseManejadorCli import ManejadorCli
from claseManejadorRep import ManejadorRep

def menu():
    print("----MENU----")
    print("1- Punto A")
    print("2- Punto B")
    print("3- Punto C")
    print("4- Punto D")
    print("0- Salir")
    print("------------")
    print("\n")
    op = int(input("Opcion >"))

    while op != 0:
        if op == 1:
            dni = int(input("DNI >"))
            ManCli.puntoA(dni)
        if op==2:
            pat = input("Patente >")
            ManCli.puntoB(pat)
        if op == 3:
            print("-----LISTADO-----")
            ManCli.puntoC()
        if op == 4:
            ManCli.puntoD()

        print("----MENU----")
        print("1- Punto A")
        print("2- Punto B")
        print("3- Punto C")
        print("4- Punto D")
        print("0- Salir")
        print("------------")
        print("\n")
        op = int(input("Opcion >"))

if __name__ == '__main__':
    ManCli = ManejadorCli()
    ManCli.testCliente()
    ManRep= ManejadorRep()
    ManRep.testRep()

    menu()

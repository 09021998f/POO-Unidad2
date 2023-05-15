from ManejadorEvaluaciones import ManejadorEv
from ManejadorFederados import ManejadorFed

def menu():
    print("\n")
    print("----MENU----")
    print("1- Punto A")
    print("2- Punto B")
    print("3- Punto C")
    print("4- Punto D")
    print("0- Salir")
    print("------------")
    print("\n")
    op = int(input("Opcion >"))

    while(op != 0):
        if(op == 1):
            print("\n")
            est = input("L: libre E: escuela\nOpcion >")
            mE.puntoA(est)
            print("\n")
        elif( op == 2):
            print("\n")
            print("------------\nParticipante con mayor puntuacion")
            mE.puntoB()
            print("\n")
         
        
        elif(op == 3):
            print("\n")
            print("--------------\nParticipantes:")
            print("\n")
            mE.puntoC()
        
        elif( op== 4):
            print("\n")
            dni = int(input("Dni: "))
            est = input("Estilo: ")
            print("Puntajes de ", dni)
            print("\n")
            mE.puntoD(dni,est.upper())

        
        print("\n")
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
    
    mE = ManejadorEv()
    mE.testEv()
    

    menu()
    print("---PROGRAMA TERMINADO----")





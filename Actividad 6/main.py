from claseViajero import ViajeroFrecuente
import csv




def creaListaViajeros(lista):
    archi = open('viajeros.csv')
    reader = csv.reader(archi, delimiter=";")
    for fila in reader:
        nv = int(fila[0])
        dni = fila[1]
        nom = fila[2]
        ap = fila[3]
        ma = int(fila[4])
        viajero = ViajeroFrecuente(nv,dni,nom,ap,ma)
        lista.append(viajero)



if __name__=='__main__':
    lista = []
    creaListaViajeros(lista)
    
    
    
    i=0
    millas=0
    millas=lista[0].getTotalMillas()
    #print(millas)
    #print(lista)
    lista.sort()
    print("*"*60)
    print(lista)

    
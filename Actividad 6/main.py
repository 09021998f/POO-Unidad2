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
    print(lista)
    #Ej1
    maxMillas= max(lista)
    for i in lista:
        if i > maxMillas:
            viajero = i
    print(i)
    
    #Ej2
    print(lista[0] + 5000)
    #Ej3
    print(lista[1] - 1000)

    

    
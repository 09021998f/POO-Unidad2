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


if __name__ == '__main__':
    lista = []
    creaListaViajeros(lista)
    #Ej1
    if 98046 == lista[0]:
        print("Mismo valor de millas")
    else:
        print("No tienen el mismo valor de millas")

    if lista[0] == 98046:
        print("Mismo valor de millas")
    else:
        print("No tienen el mismo valor de millas")

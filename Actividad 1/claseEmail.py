import csv
class Email:
    __idC = ""
    __dom = ""
    __td= ""
    __cont="" 
    
    def __init__(self, idC, dom, td, cont = 1234):
        self.__idC = idC
        self.__dom = dom
        self.__td = td
        self.__cont = cont
    def __str__(self):
        return f'Cuenta: {self.__idC}\nDominio: {self.__dom}\nTipo: {self.__td}\nContraseña: {self.__cont}\n***********' 

    def retornaEmail(self):
        return f'{self.__idC}@{self.__dom}{self.__td}'
    
    def getDominio(self):
        return self.__dom
    
    def getContrasenia(self):
        return self.__cont
    
    def crearCuenta(self, dir):
        i = dir.index("@")
        self.__idC = dir[:i]
        xi = dir.index(".")
        self.__dom = dir[i+1:xi]
        self.__td = dir[xi:]

    def getEmail(self, dir, nom):
        if(dir == self.retornaEmail()):
            print(nom, "enviaremos un email a su correo", self.retornaEmail())
        else:
            print("No se encontro email")

    def cambioContraseña(self, contr):
        if(contr == self.getContrasenia()):
            
            self.__cont == int(input("Ingrese contraseña nueva: "))
        else:
            print("XXContraseña incorrectaXX")

        return f'**Contraseña actualizada**\n  {self.__cont}'     
    


class ManejadorEmail:
    __lista = []

    def __init__(self):
        self.__lista = []
    def agregarEmail(self, unaCuenta):
        self.__lista.append(unaCuenta)

    def testEmails(self):
        archi = open('emails.csv')
        reader = csv.reader(archi, delimiter=";")
        for fila in reader:
            correo = fila[0]
            i = correo.index("@")
            cuenta = correo[:i]
            xi = correo.index(".")
            dom= correo[i+1:xi]
            td= correo[xi:]
            unaCuenta = Email(cuenta, dom, td, 1234)
            self.agregarEmail(unaCuenta)
        archi.close()
        
    def __str__(self):
        s = ' '
        for fila in self.__lista:
            s += str(fila) + '\n'
        return s

        
        


    
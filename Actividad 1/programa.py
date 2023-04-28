from claseEmail import Email
from claseEmail import ManejadorEmail
import csv
import os
if __name__ == '__main__':
    #objeto = Email("facucabj","google","com",1234)
    """
    nombre = input("Nombre:")
    correo = input("Correo: ")
    objeto.crearCuenta(correo)
    """
    """
    print("**Cuenta**")
    print(objeto)
    print("*"*10)
#   objeto.getEmail(correo, nombre)
    cont=int(input("Contraseña: "))
    objeto.cambioContraseña(cont)
    """
    #cwd = os.getcwd()  # Get the current working directory (cwd)
    #files = os.listdir(cwd)  # Get all the files in that directory
    #print("Files in %r: %s" % (cwd, files)) 
    
    mE = ManejadorEmail()
    mE.testEmails()
    print(mE)
    dom = input("Dominio: ")
    print(mE.getCantObj(dom))
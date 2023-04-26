

from claseEmail import Email

if __name__ == '__main__':
    objeto = Email("Facucabj", "google", "com", "1234" )
    print(objeto.retornaEmail())
    print(objeto.getDominio())
    
    #correo = input("ingrese su correo de email: ")
    objeto.crearCuenta("batmancat156@hotmail.com")

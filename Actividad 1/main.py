

from claseEmail import Email

if __name__ == '__main__':
    objeto = Email("Facucabj", "google", "com", "12346" )
    print(objeto)
    print(objeto.retornaEmail())
    print(objeto.getDominio())
    
    #correo = input("ingrese su correo de email: ")
    objeto.crearCuenta("batmancat156@hotmail.com")
    print("*"*30)
    print(objeto)

# POO
Actividades de la materia programacion orientada a objetos unidad 2
Facultad de Ciencias Exactas, Fisicas y Naturales
//****Ejercicios***//

         //****Ejercicio 1****//
Defina una clase “Email” con los siguientes atributos: idCuenta, dominio, tipo de dominio y contraseña (todos estos datos se ingresan por teclado). Y los siguientes métodos:

a- El constructor.

b- Método “retornaEmail()” que construye una dirección e-mail con los valores de los atributos de Email. Por ejemplo:

idCuenta.: alumnopoo

dominio: gmail

tipoDominio: com

Resultado devuelto por retornaEmail: alumnopoo@gmail.com

c- Método “getDominio()”, que retorna el dominio.

d- Método “crearCuenta(), crea una cuenta a partir de una dirección de correo que recibe como parámetro.

Implemente un programa que permita:

1- Ingresar el nombre de una persona y su dirección de e-mail (instancia de la clase Email) y luego imprima el siguiente mensaje:

Estimado <nombre> te enviaremos tus mensajes a la dirección <dirección de correo>.

2- Para la instancia creada en el ítem anterior, modificar la contraseña, teniendo en cuenta que se debe ingresar la contraseña actual, y ésta debe ser igual a la registrada en la instancia. Luego se debe ingresar la nueva contraseña y realizar la modificación correspondiente.

3- Crear un objeto de clase Email, a partir de una dirección de correo, como por ejemplo: informatica.fcefn@gmail.com, wicc2023@unsj-cuim.edu, juanLiendro1957@yahoo.com, etc.

4- a) Leer de un archivo separado por comas 10 direcciones de email, crear las cuentas correspondientes, solo para las direcciones válidas, para las no válidas, mostrar mensaje de error indicando la dirección de email incorrecta.  b) Ingresar un dominio e indicar cuántos objetos de la clase Email, tienen dominio igual al ingresado. c) Construya el diagrama de secuencia correspondiente.

            //****Ejercicio 2****//
En una aerolínea ofrece una promoción a sus viajeros frecuentes que consiste en acumular puntos por los viajes que realizan, pudiendo luego recibir beneficios a través del canje de puntos.

Métodos:
a- El constructor.
b- “cantidadTotaldeMillas”, retorna la cantidad de millas acumuladas.
c- “acumularMillas”, recibe como parámetro la cantidad de millas recorridas, las suma en el atributo correspondiente y retorna el valor del atributo actualizado.
d- “canjearMillas”, recibe como parámetro la cantidad de millas a canjear. Para utilizar las millas debe verificarse que la cantidad a canjear sea menor o igual a la cantidad de millas acumuladas, caso contrario mostrar un mensaje de error en la operación. Retorna el valor de la cantidad de millas acumuladas.

Implemente un programa que:

1- Leer de un archivo separado por comas los datos para crear instancias de la clase ViajeroFrecuente, y almacenarlas en una lista.

2- El usuario ingresa por teclado un número de viajero frecuente, el sistema presente un menú con las siguientes opciones:

a- Consultar Cantidad de Millas.

b- Acumular Millas.

c- Canjear Millas.

3- Represente el almacenamiento en memoria para la lista cargada con 4 viajeros.

4- Realice el Diagrama de Secuencia que corresponde a cada una de las siguientes funcionalidades:
4.1- El usuario elige la opción Acumular Millas, el sistema solicita el número de viajero frecuente y la cantidad de millas, el sistema busca el viajero, si lo encuentra acumula las millas ingresadas, e informa el nuevo total de millas acumulada; si el sistema no encuentra el viajero frecuente, informa al usuario de tal situación.

4.2- El usuario elige la opción Canjear Millas, el sistema solicita el número de viajero frecuente y la cantidad de millas a canjear, el usuario ingresa número de viajero frecuente y cantidad de millas a canjear, el sistema busca el viajero frecuente, si lo encuentra, verifica que la cantidad de millas acumuladas alcancen  para el canje, si no alcanzan informa la situación al usuario, si alcanzan hace el canje e informa al usuario que pudo realizar el canje y muestra la nueva cantidad de millas acumuladas; si el viajero frecuente no existe, el sistema informa al usuario de tal situación.

        //****Ejercicio 3****//

e necesita desarrollar una aplicación que procese la información de las variables meteorológicas temperatura, humedad y presión atmosférica. El registro de estas variables se hace cada una hora durante todos los días del mes. Esto se guarda en un archivo de texto separado con coma que contiene los siguientes datos: número de día, hora, valor de la variable temperatura, valor de la variable humedad y valor de la variable presión atmosférica. Se genera un archivo por cada mes.

Defina la clase “Registro” que posea como atributos los valores de las tres variables meteorológicas que se registran.

Implemente un programa que:

1.    Defina una lista bidimensional en la que se almacene el registro de las variables meteorológicas (instancia de la clase Registro) para cada día del mes, por cada hora.

2.    Almacene en la lista bidimensional los datos registrados en el archivo.

3.    Presente un menú de opciones permita realizar las siguientes tareas:

3.1.        Mostrar para cada variable el día y hora de menor y mayor valor.

3.2.        Indicar la temperatura promedio mensual por cada hora.

3.3.        Dado un número de día listar los valores de las tres variables para cada hora del día dado. El listado debe tener el siguiente formato.


          //****Ejercicio 5****//

Un concesionario de automóviles ofrece distintos planes de ahorro y se requiere la definición de una clase “PlanAhorro” que represente a cada uno de ellos.

Los datos que es necesario registrar son: código del plan, modelo y versión del vehículo, valor del vehículo, cantidad de cuotas del plan, cantidad de cuotas que debe tener pagas para licitar el vehículo (los últimos dos atributos son los mismos para todos los planes).

El primer día hábil del mes se actualiza el valor del vehículo.

El importe de la cuota se calcula:

valor cuota = (importe vehículo/cantidad de cuotas) + importe vehículo * 0.10

Implemente un programa que: 

1-      Lea desde un archivo separado con “;” los datos de los planes y genere una lista que almacene instancias de la clase “PlanAhorro”.

2-      Presente un menú de opciones permita:

a.       Actualizar el valor del vehículo de cada plan. Para esto se muestra el código del plan, el modelo y versión del vehículo, luego se ingresa el valor actual del vehículo y se modifica el atributo correspondiente.

b.      Dado un valor, mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado.

c.       Mostrar el monto que se debe haber pagado para licitar el vehículo (cantidad de cuotas para licitar * importe de la cuota).

d.      Dado el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar.


          //****Ejercicio 6****//
Dada la clase ViajeroFrecuente definida en el ejercicio 2, resolver lo siguiente:

1-    Determinar el/los viajero/s con mayor cantidad de millas acumuladas. Para distinguir entre dos objetos ViajeroFrecuente cuál posee mayor cantidad de millas acumuladas, sobrecargue el operador relacional mayor (> o  __gt__ en python).

2-    Acumular millas usando la sobrecarga del operador binario suma(+), obteniendo como resultado de la suma una instancia de la clase ViajeroFrecuente. Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, la función de acumular millas se resuelve de la siguiente forma v = v + 100.

3-    Canjear millas usando la sobrecarga del operador binario resta(-),obteniendo como resultado de la resta una instancia de la clase ViajeroFrecuente. Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, la función de canjear millas se resuelve de la siguiente forma v = v - 100.


                //****Ejercicio 7****//
Dada la clase ViajeroFrecuente definida en el ejercicio 2, resolver lo siguiente:

1-    Determinar el/los viajero/s con mayor cantidad de millas acumuladas. Para distinguir entre dos objetos ViajeroFrecuente cuál posee mayor cantidad de millas acumuladas, sobrecargue el operador relacional mayor (> o  __gt__ en python).

2-    Acumular millas usando la sobrecarga del operador binario suma(+), obteniendo como resultado de la suma una instancia de la clase ViajeroFrecuente. Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, la función de acumular millas se resuelve de la siguiente forma v = v + 100.

3-    Canjear millas usando la sobrecarga del operador binario resta(-),obteniendo como resultado de la resta una instancia de la clase ViajeroFrecuente. Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, la función de canjear millas se resuelve de la siguiente forma v = v - 100.


          //****Ejericio 8****//
Defina una clase “Conjunto” que represente un conjunto matemático de números enteros.

Implemente un programa que presente un menú de opciones que permita lo siguiente:

1- La unión de dos conjuntos, para ello sobrecargue el operador binario suma (+). Teniendo en cuenta que la unión es un nuevo conjunto que posee los elementos de ambos conjuntos, en caso de haber elementos repetidos solo aparecen una vez en el resultado. Ejemplo: Sea A={1,2,3,4} y B= {3,6,9}, A+B = {1,2,3,4,6,9}

2- La diferencia de dos conjuntos, para ello sobrecargue el operador binario resta (-). Teniendo en cuenta que el resultado de la diferencia de conjuntos es un nuevo conjunto que posee los elementos del primer operando que no se encuentren en el segundo operando. Ejemplo: Sea A={1,2,3,4} y B= {3,6,9}, A-B = {1,2}

3- Verificar si dos conjuntos son iguales, para ello sobrecargue el operador “==” teniendo en cuenta que dos conjuntos se consideran iguales si tienen la misma cantidad de elementos y sus valores son iguales (sin importar el orden de los elementos).
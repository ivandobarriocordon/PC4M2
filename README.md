# PC4M2
# ¿Cuál es la diferencia entre una lista y una tupla en Python?

Diferencias entre **lista** y **tupla** :

 -La **"lista"** es mutable

 -La **tupla** es inmutable

 ## ¿Esto que **significa**?
 
Esto lo que significa es que, **a la lista tu le puedes agregar o quitar valores** con una serie de instrucciones, en cambio, a **la tupla no porque una vez creada no se puede modificar como tal**.

Una de las **formas de agregar un elemento** en un tipo de dato del tipo **lista** es la siguiente:
     -Declaracion de Variable de tipo de lista
        mi_lista = ["Naia","Ivan","Astrid","Max"]
        mi_lista.append("Xavier")
     -La otra forma de quitar en un tipo de dato del tipo **lista** es la siguiente:
        mi_lista = ["Naia","Ivan","Astrid","Max"]
        mi_lista.remove("Naia")
    
   La sintaxis que utilizamos para añadir que es **".append"** y **".remove"** la primera como hemos visto **sirve para añadir**, esto **lo podriamos utilizar en una base de datos para poder añadir información** y la segunda que es la sintaxis que **utilizariamos para sustraer/quitar un elemento de una lista** servíria por ejemplo **para quitar un string o un integer o cualquier tipo de dato que se pueda almacenar en una lista** para despues añadir otra sintaxis que por ejemplo nos permita añadir 
# ¿Cuál es el orden de las operaciones?

El orden de las operaciones en Python viene definido al igual que en la mayoria de lenguajes de programacion a la hora de hacer operaciones por **el modelo PEMDAS** que **es un orden a la hora de como hacer las operaciones cuando tenemos distintos operadores en una operación para obtener un resultado.** PEMDAS **signfica**:

**-P: Parentesis**
**-E: Exponentes**
**-M: Multiplicación**
**-D: Division**
**-A: Adicción (Suma)**
**-S: Sustracción(Resta)**

**Existe una variación de este sistema en el cual se intercambia la M por la D lo cual sería PEDMAS y hace referencia a cambiar el orden de multiplicar y dividir por dividir y multiplicar.**


# ¿Qué es un diccionario Python?
Un diccionario es **una estructura de dato que se utiliza para almacenar pares de datos clave-valor.** 

Esto lo que quiere decir **es que cada dato tiene una clave única para acceder al valor asociado**, asi mismo, esto lo podemos imaginar como un diccionario al uso en el que consultamos palabras claves **en las que encontramos la palabra que buscamos y el valor es su significado**. 

Un ejemplo si tenemos un diccionario de nombres de personas y edades, en este ejemplo **el nombre sería la clave y la edad sería el valor asociado**. 

**Puedes utilizar la clave (nombre) para buscar y obtener el valor correspondiente (edad) de manera eficiente.**

La sintaxis de un diccionario podría ser la siguiente:

persona_edades:{ 
    "Nombre": "Ivan", 
    "edad":22, 
    "ciudad": "Portugalete" 
    }

En esta sintaxis que he puesto **los datos clave serian "Nombre", "edad" y "ciudad" y los valores de cada uno serían "Ivan", 22 y "Portugalete"**

# ¿Cuál es la diferencia entre el método ordenado y la función de ordenación?

La diferencia entre el método ordenado y la función de ordenacion es que la primera que hemos mencionado solo se puede aplicar a el tipo de dato de lista y además modifica la lista original ya que cambia su orden de manera alfabetica si son strings con palabras o alfanumerica si contiene numeros. La segunda que hemos mencionado anteriormente que es una función, se puede aplicar a cualquier dato iterable y además devuelve una lista ordenada sin modificar la original.

# ¿Qué es un operador de reasignación?
**Es un simbolo especial** que **se usa para cambiar el valor de una variable existente,** esto lo que permite **es actualizar o cambiar el valor de una variable en función de su valor actual y otro valor especifico.** 

Los operadores de reasignacion  mas comunes son los siguientes
 -(=) Se utiliza para **asignar un valor a una variable.** 
 -(+=)Se utiliza para **sumar un valor a una variable existente y asignar el resultado a la misma variable.**
 -(-=)Se utiliza para **restar un valor de una variable existente y asignar el resultado a la misma variable.**
 -(*=)Se utiliza para **multiplicar una variable existente por un valor y asignar el resultado a la misma variable.**
 -(/=)Se utiliza para **dividir una variable existente por un valor y asignar el resultado a la misma variable.**
 Ejemplos de como usariamos cada uno:

 ## Suma
 suma = 10
 suma += 5
 print(suma)  # Output: 15

 ## Resta
 resta = 20
 resta -= 7
 print(resta)  # Output: 13

 ## Multiplicación
 multiplicacion = 20
 multiplicacion /= 4
 print(multiplicacion)  # Output: 5.0

 ## Division
 Division= 20
 Division /= 4
 print(Division)  # Output: 5.0

# estructura_de_datos
## rainer gael rivera rodriguez
### estructura de datos# estrucutra_de_datos



### unidad 2

##conceptos

lista: una lista es una colección o secuencia ordenada de elementos donde cada elemento puede identificarse por su posición o índice. Las listas son una de las estructuras de datos más básicas y fundamentales en la programación, y se utilizan para almacenar y organizar datos de manera eficiente.

Diccionario: un diccionario es una colección de datos que permite almacenar y recuperar información de manera eficiente mediante una clave única asociada a cada elemento. A diferencia de las listas, donde los elementos se organizan por índices, en los diccionarios se accede a los datos mediante claves.


# diferencias entre diccionarios y listas

Organización de Datos:

En una lista, los elementos se almacenan en un orden secuencial y se accede a ellos mediante un índice numérico. La posición de un elemento en la lista es importante.
En un diccionario, los elementos se almacenan como pares clave-valor, y se accede a ellos mediante la clave asociada. La posición no es relevante, ya que los elementos no tienen un orden predefinido.
Acceso a los Elementos:

En una lista, los elementos se acceden mediante índices numéricos. Por ejemplo, mi_lista[0] accede al primer elemento de la lista.
En un diccionario, los elementos se acceden mediante claves. Por ejemplo, mi_diccionario['clave'] accede al valor asociado con la clave 'clave'.
Mutabilidad:

Las listas suelen ser mutables, lo que significa que puedes cambiar, agregar o eliminar elementos después de haber creado la lista.
Los diccionarios también son mutables. Puedes modificar valores existentes, agregar nuevos pares clave-valor o eliminar elementos.
Tipo de Claves:

En una lista, los elementos se acceden mediante índices numéricos enteros, empezando desde 0.
En un diccionario, las claves pueden ser de cualquier tipo inmutable, como cadenas, números o tuplas. Esto proporciona flexibilidad en la forma en que se accede a los datos.
Orden:

En general, el orden de los elementos en una lista es significativo. El primer elemento es diferente del segundo, y así sucesivamente.
En un diccionario, el orden de los elementos no se garantiza. Sin embargo, a partir de Python 3.7, la implementación estándar de Python preserva el orden de inserción de los elementos en un diccionario.

Pilas: Una pila es una estructura de datos lineal que sigue el principio de "último en entrar, primero en salir" (LIFO, por sus siglas en inglés, Last In, First Out). Esto significa que el último elemento que se agrega a la pila es el primero en ser eliminado. Imagina una pila de platos: puedes agregar un nuevo plato en la parte superior y retirar o agregar más platos solo desde la parte superior.

pilas estaticas: Las pilas estáticas son una implementación específica de las pilas en programación que utiliza un arreglo (array) de tamaño fijo para almacenar elementos. A diferencia de las pilas dinámicas, que pueden crecer o decrecer de tamaño durante la ejecución del programa, las pilas estáticas tienen un tamaño predeterminado y no cambia una vez que se ha creado.

pilas dinamicas: Las pilas dinámicas son una implementación de las pilas en programación que utiliza memoria dinámica para almacenar elementos y puede crecer o decrecer según sea necesario durante la ejecución del programa. A diferencia de las pilas estáticas, cuyo tamaño se determina en tiempo de compilación, las pilas dinámicas pueden adaptarse a las demandas del programa en tiempo de ejecución.

colas: Una cola es una estructura de datos que sigue el principio de "primero en entrar, primero en salir" (FIFO, por sus siglas en inglés, First In, First Out). Esto significa que el primer elemento que se agrega a la cola es el primero en ser eliminado. Imagina una cola en un supermercado: la primera persona en llegar es la primera en ser atendida.

# colas dinamicas y estaticas

Las colas dinámicas y estáticas son dos formas de implementar colas en programación, y se diferencian principalmente en la forma en que gestionan la memoria para almacenar elementos.


lenguaje R: R es un lenguaje de programación y un entorno de software especializado en estadísticas y análisis de datos. Fue desarrollado por Ross Ihaka y Robert Gentleman en la Universidad de Auckland, Nueva Zelanda.

lenguaje Python: Python es un lenguaje de programación de alto nivel, interpretado, y de propósito general. Fue creado por Guido van Rossum y lanzado por primera vez en 1991. A lo largo de los años, Python se ha convertido en uno de los lenguajes de programación más populares y ampliamente utilizados en el mundo. 

lenguaje javaScript: JavaScript es un lenguaje de programación de alto nivel, interpretado y orientado a objetos, diseñado principalmente para el desarrollo de aplicaciones web. Fue creado por Brendan Eich mientras trabajaba en Netscape y se introdujo por primera vez en 1995. A lo largo de los años, JavaScript ha evolucionado para convertirse en un lenguaje de programación ampliamente utilizado, no solo en el desarrollo web, sino también en otros contextos, como el desarrollo de servidores (Node.js) y aplicaciones móviles.


------------------------------------------------------------------------------------------------------------------------------------------------

Estructura de datos: es la clasificacion de datos segun sus caracteristicas puede tratarse de una cadena de un numero, etc.

Algoritmo: es cualquier cosa que funcione paso a paso, donde se puede describir su ambiguedad y hacen referencia a una computadora
en particular, y ademaas tiene un limite fijo en cuanto a la cantidad de datos que se pueden leer/ escribir en un solo paso.

Estructura de datos lineales: son aquellas en los cuales en las que los elementos ocupan lufares sucesivos en la estructura y cada
uno de ellos tienen un sucesor un unico predecesor.

Estructura de datos no-lineaes: son aquellas en las cuales que cada elemento puede estar entrelassdo a cualquier otro componente.

Estructura de datos dinamica: una se considera dinamica si para su creacion  se van generando o eliminando elementos al momento de
de su ejecucion.

Estructua de datos estaticos: son aquellas en la que el tamaño ocupado en la memoria se define antes de que el programa se ejecute 
y no pueda modificarse mientraas se ejecute.
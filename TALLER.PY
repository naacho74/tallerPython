import math
# #Realizar un programa que conste de una clase llamada Estudiante que
# #tenga como atributos el nombre y la nota del alumno. Definir los
# #métodos para inicializar sus atributos (_init_), imprimirlos y mostrar un
# #mensaje con el resultado de la nota y si ha aprobado o no.
#
#
# class Estudiante:
#     def __init__(self,Nombre,Nota):
#         self.nombre=Nombre
#         self.nota=Nota
#
#     def informar(self,):
#         print(f"el nombre del estudiante es {self.nombre}")
#         print(f"la nota del {self.nombre} es {self.nota}")
#
#     def mostrar_nota(self):
#         if self.nota>=3:
#             print(f"el estudiante {self.nombre} obtubo {self.nota} por lo tanto Aprobo")
#         elif self.nota>5:
#             print("Error en la nota. validar es entre 0 y 5")
#         else: print(f"el estudiante {self.nombre} reprovo con una nota de {self.nota}")
#
#
#
# estudiante1= Estudiante("juan",2.6)
# estudiante1.informar()
# estudiante1.mostrar_nota()
#
#
# """
# Realizar un programa que tenga una clase Persona con las siguientes
# características. La clase tendrá como atributos el nombre y la edad de
# una persona. Implementar los métodos necesarios para inicializar los
# atributos, mostrar los datos e indicar si la persona es mayor de edad o
# no.
# """
#
# class Persona:
#     def __init__(self, Nombre, Edad):
#         self.nombre = Nombre
#         self.edad = Edad
#
#     def ver_datos(self):
#         print(f"Nombre {self.nombre}")
#         print(f"Edad {self.edad}")
#
#         if self.edad >= 18:
#             print(f"{self.nombre} Es mayor de edad.")
#         else:
#             print(f"{self.nombre} Es menor de edad.")
#
#
#
#
# persona1 = Persona("Carlos", 17)
# persona1.ver_datos()
#

"""
Realizar un programa que se llame raíz cuadrada, la clase tendrá como
atributos que usted considere necesarios, implementar los métodos o
los atributos necesarios, mostrar los datos e indicar cuando el numero
sea negativo un mensaje donde se indique que el número debe ser
positivo, de lo contrario muestre la raíz cuadrada del número."""

# class RaizCuadrada:
#     def __init__(self, Numero):
#         self.numero = Numero
#
#     def la_raiz_cuadrada(self):
#         if self.numero < 0:
#             print("El número debe ser positivo.")
#         else:
#             raiz = math.sqrt(self.numero)
#             print("La raíz cuadrada del número es:", raiz)
#
#
# numero = float(input("Ingrese un número: "))
# raizCuadrada = RaizCuadrada(numero)
# raizCuadrada.la_raiz_cuadrada()
#

"""
Desarrollar un programa que cargue los datos de un triángulo.
Implementar una clase con los métodos para inicializar los atributos,
imprimir el valor del lado con un tamaño mayor y el tipo de triángulo
que es (equilátero, isósceles o escaleno) y sus ángulos (Acutángulo,
rectángulo, obtusángulo)."""


# class Triangulo:
#     def __init__(self, lado1, lado2, lado3):
#         self.lado1 = lado1
#         self.lado2 = lado2
#         self.lado3 = lado3
#
#     def obtener_lado_mayor(self):
#         if self.lado1 >= self.lado2 and self.lado1 >= self.lado3:
#             return self.lado1
#         elif self.lado2 >= self.lado1 and self.lado2 >= self.lado3:
#             return self.lado2
#         else:
#             return self.lado3
#
#     def determinar_tipo_triangulo(self):
#         if self.lado1 == self.lado2 == self.lado3:
#             return "Equilátero"
#         elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
#             return "Isósceles"
#         else:
#             return "Escaleno"
#
#
#     def clasificar_angulo(self, angulo):
#         if angulo == 90:
#             return "Rectángulo"
#         elif angulo < 90:
#             return "Acutángulo"
#         else:
#             return "Obtusángulo"
#
#     def imprimir_datos(self):
#         print("Lado mayor:", self.obtener_lado_mayor())
#         print("Tipo de triángulo:", self.determinar_tipo_triangulo())
#
# lado1 = float(input("Ingrese la longitud del lado 1: "))
# lado2 = float(input("Ingrese la longitud del lado 2: "))
# lado3 = float(input("Ingrese la longitud del lado 3: "))
#
# triangulo = Triangulo(lado1, lado2, lado3)
# triangulo.imprimir_datos()


"""
Realizar un programa realizado por usted en donde aplique:
abstracción, herencia, polimorfismo y encapsulamiento. (no puede ser
copiado de internet."""



class Alimento:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def obtener_nombre(self):
        return self.nombre

    def obtener_precio(self):
        return self.precio

    def obtener_descripcion(self):
        pass


class Pizza(Alimento):
    def __init__(self, nombre, precio, ingredientes):
        super().__init__(nombre, precio)
        self.ingredientes = ingredientes

    def obtener_descripcion(self):
        return f"La pizza {self.nombre} su valor es de ${self.precio} y tiene los siguientes ingredientes: {', '.join(self.ingredientes)}."


class Ensalada(Alimento):
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo = tipo

    def obtener_descripcion(self):
        return f"La ensalada {self.nombre} tiene un valor de ${self.precio} y es de tipo {self.tipo}."


# Ejemplo de uso
pizza_margarita = Pizza("Margarita", 30000, ["tomate", "queso", "albahaca"])
ensalada_cesar = Ensalada("César", 12000, "César tradicional")

print(pizza_margarita.obtener_descripcion())
print(ensalada_cesar.obtener_descripcion())


# """
# punto 1
#
# Crear una tupla con números que usted desee, crear dos tuplas vacías llamadas par
# y la otra impar. A través de un ciclo for recorrer la tupla numérica si el numero
# evaluado es para ingresar el valor a la tupla par, de lo contrario insertar a la tupla
# impar.
# """
#
# tuplaPar=()
# tuplaImpar=()
# tuplaNumerica=()
#
# numeros=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
#
#
# tuplaImpar=list(tuplaImpar)
# tuplaPar=list(tuplaPar)
# for numero in numeros:
#
#     if(numero%2==0):
#
#         tuplaPar.append(numero)
#     else:
#
#         tuplaImpar.append(numero)
#
# print(tuple(tuplaPar))
# print(tuple(tuplaImpar))
#
#
# """punto 2
#
# Crear una tupla con diferentes valores numéricos o cadenas de texto, crear un
# programa que muestre el elemento mayor y menor de la tupla usando la función
# correspondiente"""
#
# tupla2 = (20,4,9,6,-10,4,-1,0)
#
# print("Mayor:", max(tupla2))
# print("Menor:", min(tupla2))
#
#
# """
# punto 3
#
# Crea una tupla numérica, pide al usuario que ingrese un número y crea un programa
# que cuente cuantas veces está el numero ingresado en la tupla, de lo contrario
# muestre que el número no se encuentra.
# """
#
# numeros = (10,2,2,6,8,5,4,3,20,15,7,2,1,0,7,3,4,5,6)
# numero = int(input("Dame un numero: "))
#
# print("Numero de repeticiones del numero ",numero," es ", numeros.count(numero))
#
# """
# punto 4
#
# Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el
# teléfono. Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere
# insertar más. No se podrán meter nombres repetidos. Debe imprimir el diccionario
# creado.
# """
#
# diccionario = {}
#
# salir = False
#
# while(not salir):
#
#     nombre = input("Introduce el nombre: ")
#     telefono = input("Introduce el telefono: ")
#
#     if(nombre not in diccionario):
#         diccionario [nombre] = telefono
#         print("Añadido el contacto")
#     else:
#         print("El nombre esta repetido")
#
#     respuesta = input("¿Quieres salir? (YES/NO)")
#     if (respuesta == "YES"):
#         salir = True
#
#     print(diccionario)
#
#
#
# """
# punto 5
#
# Teniendo en cuenta el punto anterior, crea un programa que solicite al usuario la
# clave(usuario) y muestre el teléfono correspondiente
# """
#
# claveIngresada=input("ingresa el nombre de usuario: ")
#
# vuelta=True
#
# while(vuelta==True):
#
#     for clave,valor in diccionario.items():
#
#         if(claveIngresada==clave):
#          print("El telefono de ",clave," es ",valor)
#         else:
#              print("usuario no existente")
#         respuestaUser=input("¿Deseas salir? Y/N: ")
#
#         if(respuestaUser=="Y"):
#             vuelta=False
#         else:
#             claveIngresada = input("ingresa el nombre de usuario: ")
#
#
# """
# punto 6
#
# Crea una tupla con valores ya predefinidos del 1 al 10, pide un índice por teclado y
# muestra los valores de la tupla.
# """
#
# tuplaIndice = (1,2,3,4,5,6,7,8,9,10)
# indice = int(input("Dame un indice: "))
# if indice >= 0 and indice<len(tuplaIndice):
#     print(tuplaIndice[indice])
# else:
#     print("Indice no valido")


"""
Taller listas

punto 1

Encuentra los errores en los siguientes ejemplos de lista:

"""
#a.
lista = ["verde","amarillo","azul"]
#a.2
lista = ["verde","amarillo","azul"]
print(lista[0])

#b.
lista = ["verde","amarillo","azul"]
print(lista[0])
print(lista[2])



"""
punto 2


Crea una lista vacía llamada departamentos Colombia, pida al usuario
la cantidad de departamentos a ingresar, a través de un ciclo for pida
al usuario que ingrese el departamento de Colombia que desee,
agregue esta información a la lista y luego esta sea ordenada en orden
descendente.

a. Se debe imprimir la lista con los valores organizados de forma
descendentes.

b. Debe imprimir además los 2 últimos departamentos ingresados
"""

departamentos_Colombia = []

numero_departamentos = int(input("Ingrese la cantidad de departamentos: "))

for departamento in range(0,numero_departamentos):

    departamento = input("Ingresa el nombre del departamento: ")
    departamentos_Colombia.append(departamento)

reverse = list(reversed(departamentos_Colombia))
lista_reverse_2 = [reverse[0],reverse[1]]
print(reverse)
print(lista_reverse_2)



"""punto 3

crea una lista vacía llamada números, a través de un bucle for o while
pide al usuario que ingrese números enteros, agrega los números a la
lista y luego ordena esta de forma ascendente y descendente. Mostrar
ambas listas (ascendente y descendente)

"""

numeros_lista=[]
cantidad_numeros = int(input("Ingresa una cantidad de numeros: "))
for numero in range(0,cantidad_numeros):
    numero = int(input("Ingrese el numero: "))
    numeros_lista.append(numero)

print(numeros_lista)
reverse = list(reversed(numeros_lista))
print(reverse)
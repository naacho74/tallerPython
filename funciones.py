# #crear una funcion que muestre 2 numeros en orden descendente
# """
# def ordenarDesc (num1,num2):
#     if num1>num2:
#         return num1,num2
#     elif num2>num1:
#         return num2,num1
#     else:
#         return f"{num1} esta duplicado"
#
#
# print(ordenarDesc(50,50))
#
# #recursividad: cuando la funcion se llama a si misma
#
# # imprimir los numeros del 10 al 1.
#
# def mostrarNum(num):
#    if num > 0:
#     print(num)
#     mostrarNum(num-1)
#
# mostrarNum(10)
#
# #factorial de un numero
#
# def factorial(valor):
#    if valor>1:
#         valor=valor*factorial(valor-1)
#    return valor
#
#
# print(factorial(4))
#
# """
#
# #crear una funcion que reciba un numero como arametro y devuelva true si es primo ó false si no lo es.
#
def sacarPrimo(num):
        for n in range(2, num):
            if num % n == 0:
                return False
        return True
print(sacarPrimo(3))

#utilizando la funcion del punto 1, realizar otra funcion que reciba de
# parametro una lista de numeros y devuelva solo aquellos que son primos en otra lista


lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46]

def sacarLosPrimos(lista):
    primos = []
    for num in lista:
        if  sacarPrimo(num):
            primos.append(num)
    return primos

print(sacarLosPrimos(lista))


#crear una funcion que convierta entre grados Celsius, farenheit y kelvin
# convertir a farenheit -> (c X 9/5) + 32 = f
# convertir a kelvin -> c+273.15= k
# debe recibir 3 parametros  -> valor, medida origen y medida destino
# c a f multiplica 1.8 +32
# f a c valor-32 / 1.8
# c a k valor + 273.15
# k a c valor - 273.15
# f a k valor + 459.67 / 1.8
# k a f valor * 1.8 -  459.67


def convertirGrados(valor,origen,destino):

    if origen== "c" and destino=="f":
        valorFinal=(valor*1.8)+32
        print("se convirtio de ", valor, "Celsius a ",valorFinal, " Farenheit")
    elif origen == "f" and destino =="c":
        valorFinal=(valor-32)/1.8
        print("se convirtio de " ,valor, "Farenheit a " ,valorFinal, " Celsius")
    elif origen == "c" and destino == "k":
        valorFinal=valor+273.15
        print( "se convirtio de " ,valor, " Celsius a ",valorFinal, " Kelvin")
    elif origen == "k" and destino == "c":
        valorFinal=valor-273.74
        print( "se convirtio de",valor," Kelvin a ",valorFinal, "Celsius")
    elif origen == "f" and destino == "k":
        valorFinal=(valor+459.67)/1.8
        print( "se convirtio de " ,valor, " Farenheit a ",valorFinal, " Kelvin")
    elif origen == "k" and destino == "f":
        valorFinal=(valor*1.8)-459.67
        print( "se convirtio de " ,valor, "Kelvin a " ,valorFinal, " Farenheit")
    else:print( "parametros no definidos correctamente")


convertirGrados(50,"k","c")

"""Iterando una lista con los tres valores posibles deF
temperatura que recibe la funcion del punto 3, hacer un print para cada combinacion de los mismos:"""


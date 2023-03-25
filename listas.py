# # listas
#
# lista1=[]
# lista1=[1,"hola",1.23,True,False]
#
# texto="Hola grupo"
#
# #son mutables --> se pueden modificar,eliminar,extender
# # len(lista) es para saver la longitud
#
# print(len(lista1))
#
# #agregar elementos  append()
#
# lista1.append("colecciones")
# print(lista1)
#
# # agregar eligiendo el indice
#
# lista1.insert(1,4)
#
# print(lista1)
#
# #ELIMINAR EKEMENTOS: pop(posicion), remove(elemento)
#
# lista1.pop(2)
#
# print(lista1)
#
# lista1.remove(4)
#
# print(lista1)
#
# #conocer el indice o posicion del elemento : index(elemento)
#
# print(lista1.index("colecciones"))
#
# valor= lista1.index(False)
#
# print(valor)
#
# numeros=[0,1,2,3,4,5,6,7,8,9]
#
# animales=["delfines","perro","caballo"]
#
# #extender listas o combinarlas
#
# lista1.extend(numeros)
#
# print(lista1)
#
# lista1.extend(animales)
#
# print(lista1)
#
# # eliminas los elementos de las listas con clean
#
# # recorrer listas
# index=0
# for animal in animales:
#     print(f"el animal en la posicion  {index}  es  {animal}")
#     index+=1
#
# for indice in range(len(animales)):
#     print(animales[indice]," esta en la posicion", indice)

"""
crear dos listas vacias llamadas par e impar

pedir al usuario que ingrese 2 numeros

while= si el numero 1 es menor que el numero 2 --> almacene los numeros pares 
e impares en la lista correspondiente

For= numero 1 es inicio del rango, numero 2 el final...
 los datos se almacenan en la lista correspondiente

"""

listaPar=[]
listaImpar=[]

numero1=int(input("ingrese el primer numero: "))
numero2=int(input("ingrese el segundo numero: "))

if numero2 > numero1:
    for indice in range(numero1,numero2+1):
        if indice%2==0:
            listaPar.append(indice)
        else:
            listaImpar.append(indice)

    print(listaPar)
    print(listaImpar)


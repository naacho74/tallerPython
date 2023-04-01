tuple=()
tuples=1,2,3,4
tupla=7,
print(type(tupla))
print(type(tuples))
print(type(tuple))



diccionario={}
diccionario1=dict()
print(type(diccionario))
print(type(diccionario1))
#dicc={"clave":valor,"clave":valor}
datos={"nombre":"karina","edad":24,"genero":"f","fecha_nacimiento":"24/01/96"}

datos1= dict(nombre="carlos",
             edad=24,
             genero="m",
             fecha_nacimiento="01/3/1999")

#acceder a un elemento
print(datos["edad"])

#modificar un valor
datos["nombre"]="camila"
datos["edad"]=26

print(datos)

#metodo get(): devuelve el elementode la clave

print(datos.get("genero"))

#metodo update(): actualiza el diccionario

animales={"invertebrado":"gusano","vertebrados":"elefante",
          "carnivoro":"leon","omnivoro":"ratón"}

marcas={"tenis":"nike","celular":"nokia","carro":"mazda","colchones":"comodisimos"}

animales.update(marcas)
print(animales)

#metodo pop(): elimina la clave pasada como argumento y su valor

animales.pop("carnivoro")
print(animales)

#popitem()

animales.popitem()

print(animales)

#imprimir solo claves de diccionario

print(animales.keys())

for clave in animales.keys():
    print(clave)

#imprimir solo los valores

print(animales.values())

for valor in animales.values():
    print(valor)

# imprimir tanto clave como valor

print(animales.items())

for clave, valor in animales.items():
    print(clave, "->", valor)

#eliminar todos los elementos del diccionario

animales.clear()

print(animales)




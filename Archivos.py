import os
# """
# Importancia de manejo de Archivos: manipulacion de datos externos,
#  centralizacion de la informacion, envio de datos seguros.
#
#  permisos: r (lectura), w(escritura), w+(lectura y escitura),
#  a(actualizar - agregar informacion),a+(crea archivo y si ya existe lo actualiza)
#
# """
#
# #crear archivos
#
# file=open("Archivo2.txt","w+")
#
# #para invocar y escribir en el archivo
# file.write("\n\nCursos:\nMoviles\nBases de datos\nNuevas Tecnologias")
#
# #para renombrar hay que cerrar el archivo
# file.close()
#
# #Cambiar el nombre
# #os.rename("Archivo1.txt","ArchivoNuevoNombre.txt")
#
#
# #cuando se trabaja con with no es necesario cerrar el archivo, el lo cierra automaticamente
#
# with open("archivo3.txt","r") as archivo:
#     #read() => unificada en un string
#     #readlines() => cada linea la guarda como un elemento de una lista
#     escritoDelArchivo=archivo.read()
#     print( type(escritoDelArchivo))
#
# #verifica si un archivo existe o no
# print(os.path.isfile("archivo3.txt"))
# #verificar si la carpeta existe
# print(os.path.isdir("tallerPython"))
# #conocer la ruta del proyecto
# print(os.getcwd())
# # para eliminar un arcivo
# os.remove("nombre del archivo")
#
# """
# verificar si un archivo existe, si
# existe cambiar el nobmre, de lo contrario mostrar mensaje indicando que no existe
# """

# nombreArchivo=input("estribe el nombre del archivo que quieres verificar")
#
# if(os.path.isfile(nombreArchivo)):
#     print("el archivo existe")
#     nuevoNombre=input("escribe el nuevo nombre: ")
#     os.rename(nombreArchivo,nuevoNombre)
# else: print("el archivo no existe")


with open('archivo3.txt',"r") as texto:
    lineas=texto.readlines()
    print(lineas)
    comida=[]
    precio=[]

    for renglon in lineas:
        infoArt=renglon.replace('\n','').split('#')
        print(infoArt)
        comida.append(infoArt[0])
        precio.append(infoArt[1])

print(comida)
print(precio)
print(texto.name)
print(texto.encoding)
print(texto.mode)
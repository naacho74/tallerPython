
# ejercicio 1#
print(" ejercicio # 1")
nombre= input("Digita el nombre: ")
edad = int(input("Digita la edad: "))

if edad >=18:
    print(f"{nombre} tiene {edad} años y es Mayor de edad")
else:
    print(f"{nombre} tiene {edad} años y es Menos de edad")

#ejercicio 2
print("ejercicio # 2")

dividendo= int(input("Digia el dividendo: "))
divisor= int(input("Digita el divisor: "))

resultado=dividendo/divisor

residuo=dividendo%divisor

if(residuo==0):
  print(f"la division es exacta... y el cociente es: {resultado} ")
else:
  print(f"el  residuo es {residuo} y el resultado de la division es: {resultado}")



 #ejercicio 3

  print("Ejercicio # 3")

  nombre2=input("Digite su Nombre")

  anioNacimiento=int(input("Digita el Año de Nacimiento: "))
  anioActual=int(input("Digita el anio Actual"))

  if(anioActual>anioNacimiento):
   print(f"la edad de {nombre2} es ",anioActual-anioNacimiento," años")
  else:
   print("el año de nacimiento no puede ser mayor al valor actual")




 #ejercicio 4

print("ejercicio #4")

edad=int(input("Digita la edad: "))

grupo= input("Ingresa  un grupo... sea adultos o infantes")

if edad>18 and grupo=="adultos":
  print("puedes entrar")
elif edad > 18 and grupo == "adultos":
  print("no puedes ingresar al grupo eres menor de edad")
elif edad <18 and grupo =="infantes":
  print("puedes ingresar cumples con las condiciones")
else:
  print("Esta opcion no es valida")






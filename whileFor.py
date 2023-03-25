#bucle while

# i = 0

# while i < 15:
#     print(i)
#     i += 1
#     print("ciclo terminado")


##################################################


#mostrar los numeros pares

# num = 0
# num2 = int(input("ingrese el limite de rango: "))
# while num < num2:
#     num +=1
#     if num%2==0:
#         print(num)
   
   
#####################################################   
   
#programa que solicite confirmar contraseña y confirmaciion de esta.


# contrasenia= input("ingrese su contraseña: ")
# contraseniaConfirmada= input("Confirme su contraseña: ")

# while contrasenia!=contraseniaConfirmada:
#     print("las contraseñas no coinciden... vuelve a digitar los valores")
#     contrasenia= input("ingrese su contraseña: ")
#     contraseniaConfirmada= input("Confirme su contraseña: ")
    
# print("Excelente")

##################################################################

# Hacer un programa donde el usuario escoja entre varios lenguajes de programacion(html, css, js, py) y segun la opcion escogida muestre para que sirve.





# lenguajeEscogido=0

# while lenguajeEscogido != 5:
#     lenguajeEscogido=int(input("Elige un lenguaje por su numero...  1:html  2: Css  3:JS  4:PY 5: Para salir: "))
    
#     if (lenguajeEscogido == 1):
#         print("Elegiste Html ---> Sirve para hacer las estructuras mediate etiquetas")
#     elif(lenguajeEscogido == 2):
#           print("Elegiste Css ---> sirve para dar estilo a las etiqetas cradas con html")
#     elif(lenguajeEscogido == 3):
#         print("Elegiste JavaScript ---> sirve para ")
#     elif(lenguajeEscogido == 4):
#         print("Elegiste Python ---> ")
#     elif(lenguajeEscogido == 5):
#         break    
#     else: 
#         print ("Esa Opcion no esta en el menu")
     
     
     
     
"""EJERCICIO WHILE
Hacer una calculadora en Python usando el ciclo while, teniendo en cuenta lo siguiente:
- El usuario debe ingresar los datos a tener en cuenta en las operaciones.
- La calculadora debe contener las siguientes opciones: 
o Suma
o Resta
o Multiplicación
o División: para realizar esta operación debe tener una restricción que evite que el 
usuario ingrese 0 como divisor.
o Potenciación
o Multiplicación
o Raíz cuadrada, debe especificar que el dato a ingresar debe ser entero positivo
o Cambiar números
o Salir
- Crear in código que arroje el resultado de la operación escogida por el usuario"""     


opcion=0

while opcion != 7:
    opcion=int(input("elige un Numero segun la operacion a ralizar --> 1:suma 2:resta 3:division 4:multiplicacion 5:Potenciacion 6:Raiz 7: para cambiar los numeros Cuadrada ó ingresa 7 para salir: "))
    if(opcion==7):
        break
    numero1=int(input("Digite el primer numero: "))
    numero2=int(input("Digite el segundo numero: "))
    
    
    
    if(opcion == 3 and numero2 == 0):
        print("No se puede dividir entre 0")

        while numero2 == 0:
            numero2=int(input("Digite el segundo numero ... recuerda que en Division no se puede  dividir entre 0: "))
    if opcion == 1:
         print("Elegiste Suma")
         print(f"el valor de la suma es: {numero1 + numero2}")
    elif opcion == 2:
        print("Elegiste Resta")
        print(f"el valor de la resta es: {numero1 - numero2}")
    elif opcion == 3:
        print("Elegiste Division")
        print(f"el valor de la division es: {numero1 / numero2}")
    elif opcion == 4:
        print("Elegiste Multiplicacion")
        print(f"el valor de la Multiplicacion es: {numero1 * numero2}")
        
    elif opcion == 5:
        print("Elegiste potenciacion") 
        print(f"el valor de la potenciacion  es: {numero1 ** numero2}") 
    elif opcion == 6:
        print("Elegiste Raiz Cuadrada")
        print(f"el valor de la Raiz Cuadrada de numero 1 es: {numero1**0.5}")
        print(f"el valor de la Raiz Cuadrada de numero 2 es: {numero2**0.5}")
           
    elif(opcion==7):
       break
       
       
    else: print("Opcion no valida")
            
    


     
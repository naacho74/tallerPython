#OPERADORES ARITMETICOS

numero1=23
numero2=10
print("suma: ",numero1+numero2)

num1=int(input("ingresa el primer numero: "))
num2=int(input("ingresa el segundo numero: "))


if num1>num2:
    print(f"{num1} es mayor")

else:
    print(f"{num1} es mayor")


if num1%2==0:
    print(num1, " es par")
else:
    print(num1, " es Impar")

#Impresion de in ternario
print(f"{num1} es par " if num1%2==0 else f"{num1} es impar")

#title(),upper(), lower ()

texto = "Hola Grupo!!"

mayuscula=texto.upper()
print(mayuscula)

minuscula=texto.lower()
print(minuscula)


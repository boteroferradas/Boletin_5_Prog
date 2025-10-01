# Boletin 5 Bucles
from math import factorial

# 1. Escribir un ciclo definido para imprimir por pantalla tódolos números entre 10 e 20.

# numeros = range(10,21)
#
# for n in numeros:
#     print(n)

# 2. Escribir un programa que converta un valor dado en grados Fahrenheit a grados Celsius.
# Recordade que a fórmula para a conversión é: F = 9/5 * C + 32.

# tempF = float(input("Introduzca temperatura en Farenheit"))
# tempC = tempF - 32 / 1.8
#
# print(tempC)

# 3. Utiliza o programa anterior para xerar unha táboa de
# conversión de temperaturas, dende 0º F ata 120º F, de 10 en 10.

# tF = range(0,130,10)
# for n in tF:
#     conversor = n - 32 / 1.8
#     print(conversor)

# 4. Escribir un programa que imprima tódolos
# números pares entre dous números que se lle pidan o usuario.

# n1 = int(input("Primer numero: "))
# n2 = int(input("Segundo numero: ")) + 1
# listanumeros = range(n1, n2)
# for n in listanumeros:
#     espar = n%2
#     if espar == 0:
#         print(n, "es par")
#     else:
#         print(n, "no es par")


# 5. Escribir un programa que reciba un número n por parámetro e imprima os
# primeiros n números triangulares, xunto co seu índice.
# Os números triangulares obteñense mediante a suma dos números naturales dende 1 ata n.
# É dicir, si se piden os primeros 5 números triangulares, o programa debe imprimir:

# n = int(input("Introduzca un numero: ")) + 1
# lista = range(1,n)
# contador = 0
# for numero in lista:
#     contador += 1
#     operador = numero * (numero + 1) / 2
#     print(contador, int(operador))

# 6. Escribir un programa que tome unha cantidade m de valores
# ingresados polo usuario, a cada un lle calcule o factorial e
# imprima o resultado xunto co número de orden correspondiente.

# m = int(input("Introduzca un numero: ")) + 1
# lista = range(1,m)
# contador = 0
# for n in lista:
#     contador += 1
#     operacion = factorial(n)
#     print(contador, operacion)

# 7. Escribir un programa que imprima por pantalla tódalas
# fichas de dominó, de unha por liña e sen repetir.


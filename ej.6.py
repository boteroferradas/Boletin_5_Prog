# 6. Escribir un programa que tome unha cantidade m de valores
# ingresados polo usuario, a cada un lle calcule o factorial e
# imprima o resultado xunto co número de orden correspondiente.
from math import factorial

m = int(input("Introduzca un numero: ")) + 1
lista = range(1,m)
contador = 0
for n in lista:
    contador += 1
    operacion = factorial(n)
    print(contador, operacion)
# 5. Escribir un programa que reciba un número n por parámetro e imprima os
# primeiros n números triangulares, xunto co seu índice.
# Os números triangulares obteñense mediante a suma dos números naturales dende 1 ata n.
# É dicir, si se piden os primeros 5 números triangulares, o programa debe imprimir:

n = int(input("Introduzca un numero: ")) + 1
lista = range(1,n)
contador = 0
for numero in lista:
    contador += 1
    operador = numero * (numero + 1) / 2
    print(contador, int(operador))
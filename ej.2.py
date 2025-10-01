# 2. Escribir un programa que converta un valor dado en grados Fahrenheit a grados Celsius.
# Recordade que a fórmula para a conversión é: F = 9/5 * C + 32.

tempF = float(input("Introduzca temperatura en Farenheit: "))
tempC = tempF - 32 / 1.8

print(tempC)
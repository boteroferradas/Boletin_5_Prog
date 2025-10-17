# Codifica un programa que solicite un número e visualice
# a táboa de multiplicar dese número. O programa seguirá
# pedindo números ata que o usuario pulse o número cero.


tabla = range(1, 11)

while True:
    n = int(input("Introduzca un numero: "))
    contador = 1
    if n != 0:
        for numero in tabla:
            resultado = n * contador
            print(f"{n} x {contador} = {resultado}")
            contador += 1
    else:
        print("0 no es valido")
        break
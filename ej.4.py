# 4. Escribir un programa que imprima tódolos
# números pares entre dous números que se lle pidan o usuario.

n1 = int(input("Primer numero: "))
n2 = int(input("Segundo numero: ")) + 1
listanumeros = range(n1, n2)
for n in listanumeros:
    espar = n%2
    if espar == 0:
        print(n, "es par")
    else:
        print(n, "no es par")
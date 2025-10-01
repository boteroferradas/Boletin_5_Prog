# 9. Calcula a cantidade de números negativos, positivos e ceros que
# hai nun grupo de 10 números enteiros.

n_positivos = 0
n_negativos = 0
n_soncero = 0

for n in range(-5,5):
    print(n)
    if n >= 0:
        n_positivos += 1
    elif n <= 0:
        n_negativos += 1
    elif n == 0:
        n_soncero += 1

print(f"Hay {n_positivos} numeros positivos")
print(f"Hay {n_negativos} numeros negativos")
print(f"Hay {n_soncero} numeros iguales a cero")


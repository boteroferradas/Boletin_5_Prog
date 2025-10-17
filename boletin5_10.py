# Deseña un programa que calcule o área dun rectángulo cuxa base
# e altura pides por teclado. Asegúrate que estes valores
# sexan positivos, para eso valida os datos.

base = int(input("Introduzca una base: "))
altura = int(input("Introduza unha altura: "))

if base and altura < 0:
    print("Por favor, introduzca valores positivos")
else:
    area = base * altura
    print(f"A area do triangulo e: {area}")
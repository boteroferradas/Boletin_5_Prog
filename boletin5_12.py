# Codifica un programa que lea o soldo de cada un dos
# traballadores dunha empresa e obteña o número deles que
# ganan entre 1000 e 1750 €, ámbolos dous incluídos e, a
# porcentaxe de traballadores que ganan menos de 1000 €. Tendo
# en conta que non se coñece con antelación o numero de
# traballadores da empresa e non se admiten os soldos negativos
# (utiliza como condición de fin un soldo 0).

lista_traballadores = [1700,1650,1000,980,800,1400,500,430,1350]
masde1000 = 0
mennosde1000 = 0

for n in lista_traballadores:
    if n != 0:
        if 1000 < n < 1750:
            masde1000 += 1
        elif n <= 1000:
            mennosde1000 += 1

print(f"{masde1000} traballadores ganan entre 1000 e 1750 euros")
print(f"{mennosde1000} traballadores ganan menos de 1000 euros")

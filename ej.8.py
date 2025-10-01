# 8. Modificar o programa anterior para que poida xerar fichas dun xogo que pode ter números de 0 a n.

numerodefichas = int(input("Cal e o numero maximo de fichas que queres: "))

for n in range(numerodefichas):
    for m in range(n,numerodefichas):
        print("A ficha é:",n,"|",m)
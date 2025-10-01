# 3. Utiliza o programa anterior para xerar unha táboa de
# conversión de temperaturas, dende 0º F ata 120º F, de 10 en 10.

tF = range(0,130,10)
for n in tF:
    conversor = n - 32 / 1.8
    print(conversor)
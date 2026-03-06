print("-="*20)
print("Analizador de Triangulos")
print("-="*20)
r1 = float(input("Primeiro segmento: "))
r2 = float(input("segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima podem formar triangulos")
    if r1 == r2 == r3:
        print("EQUILATERO")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("Isósceles")
    else:
        print("ESCALENO")
else:
    print("Os segmentos acima não podem formar triangulos")

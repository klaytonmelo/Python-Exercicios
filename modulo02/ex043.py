print("*** Veja seu IMC ***")

p = float(input("Digite seu peso: "))
a = float(input("Digite sua altura: "))

imc = p / (a ** 2)

print(f"O IMC dessa pessoa é {imc:.1f}")
if imc < 18.5:
    print("peso BAIXO")
elif imc < 25:
    print("Peso IDEAL")
elif imc < 30:
    print("SobrePESO")
elif imc < 40:
    print("OBESIDADE")
else:
    print("Obesidade MÓRBIDA")
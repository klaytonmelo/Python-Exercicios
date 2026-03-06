p = float(input("Digite seu peso: "))
a = float(input("Digite sua altura: "))

imc = p / (a**2)

print(f"Seu IMC é {imc:.2f}")

if imc < 18.5:
    print("abaixo do peso")
elif imc < 25:
    print("peso ideal")
elif imc < 30:
    print("sobrepeso")
elif imc <= 40:
    print("obesidade")
else:
    print("obesidade morbida")
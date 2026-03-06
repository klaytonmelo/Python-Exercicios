n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

media = (n1 + n2) / 2
print(f"sua média é: {media}")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Reculperaçao")
else:
    print("Reprovado")

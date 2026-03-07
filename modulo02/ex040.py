n1 = float(input("Primeira nota: "))
n2 = float(input("segunda nota:"))
n3 = float(input("Terceira nota: "))
n4 = float(input("Quarta nota: "))

media = (n1 + n2 + n3 + n4) / 4

print(f"A média do aluno é {media}")
if media < 7 and media >= 5:
    print("O aluno esta de RECUPERAÇÃO!")
elif media < 5:
    print("O aluno esta REPROVADO!")
else:
    print("O aluno esta APROVADO!")
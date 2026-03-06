print("veja sua categoria!")

idade = int(input("Digite sua idade: "))

if idade <= 9:
    print("Mirim")
elif idade <= 14:
    print("Infantil")
elif idade <= 19:
    print("Junior")
elif idade <= 20:
    print("Senior")
else:
    print("Master")
lanche = ("hambúrguer", "Suco", "Pizza", "Pudim", "batata frita")

for comida in lanche:
    print(f"Eu vou comer {comida}")

print("-" * 30)

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]}")

print("-" * 30)

for pos, comida in enumerate(lanche):
    print(f"eu vou comer {comida} na posiçao {pos}")



print("Comi pra caramba!")
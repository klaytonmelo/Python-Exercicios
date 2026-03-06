num = int(input("Informe um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
um = num // 1000 % 10
print(f"analisando número: {num}")
print(f"Unidade: {u}")
print(f"Desena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {um}")

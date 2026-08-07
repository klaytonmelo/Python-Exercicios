""""
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato 
Brasileiro de Futebol, na ordem de colocação. Depois mostre:

A) Apenas os 5 primeiros colocados.
B)Os ultimos 4 colocados na tabela
C)Uma lista com os times em ordem alfabética
D)Em que posição está o time Chapecoense.

"""
from rich import print
times = ("Palmeiras", "Flamengo", "Athletico-PR", "Fluminense", "Bahia", "Red Bull Bragantino", "Cruzeiro", "Botafogo", "Corinthias", "Ceará", "Grêmio", "Internacional", "Vasco da Gama", "Mirassol", "Atlético-MG", "São Paulo", "Santos", "Chapecoense", "Coritiba", "Remo")

print("[green]-[/]" * 30)
print("[blue]lista de times do Brasileirão: [/]")
for n, c in enumerate(times):
    print(f"{n + 1}. {c}")

print("[green]-[/]" * 30)

print("[blue]Os cinco primeiros são: [/]")
for n, c in enumerate(times[:5]):
    print(f"{n + 1}. {c}")

print("-" * 30)

print("[blue]Os últimos 4 colocados são: [/]")

for c in times[-4:]:
    print(f"{times.index(c) + 1}. {c}")

print("-" * 30)

print("[blue]Times em ordem alfabética: [/]")
for c in sorted(times):
    print(c)

print("[green]-[/]" * 30)

print(f"Chapecoense está na posição: {times.index("Chapecoense") + 1}")

print("[green]-[/]" * 30)

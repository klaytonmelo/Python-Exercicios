'''
faça um programa que leia um número inteiro
e diga se ele é ou não um número primo.

***********
DICA: numeros primos são aqueles que são apenas
divisiveis por um e por ele mesmo.
***********
'''
from rich import print #biblioteca rich está no mundo 4 - "python POO"

n = int(input('Digite um número: '))

tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print(f"[yellow]{c}[/]")
        tot += 1
    else:
        print(f"[red]{c}[/]")

print(f"O número {n}, foi divisivel {tot} vezes")
if tot == 2:
    print("por isso ele é PRIMO!")
else:
    print("Por isso ele não é PRIMO!")
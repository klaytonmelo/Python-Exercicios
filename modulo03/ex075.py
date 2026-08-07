"""
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. no final mostre:

A)Quantas vezes apareceu o valor 9.
B)Em que posição foi digitado o primeiro valor 3.
C)Quais foram os números pares.
"""
from rich import print

num = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))

print("[blue]-[/]" * 30)
print(f"Você digitou os valores:")
for c in num:
    print(c)

print(f"O número 9 apareceu {num.count(9)} vezes")

print("[blue]-[/]" * 30)
if 3 in num:
    print(f"O primeiro valor 3 esta na posição: {num.index(3)}")
else:
    print("[red]O número 3 não foi encontrado[/]")

print("[blue]-[/]" * 30)

print(f"[blue]Números pares digitados foram: [/]")
par = 0
for c in num:
    if c % 2 == 0:
        print(c)

print("[blue]-[/]" * 30)

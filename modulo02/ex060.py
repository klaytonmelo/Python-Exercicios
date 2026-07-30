'''
Faça um programa que leia um numero qualquer 
e mostre seu fatorial.

Ex:
5! = 5x4x3x2x1 = 120
'''
from rich import print #blibiotéca módulo 4 - POO

n = int(input('Digite um número para calcular seu Fatorial: '))
print(f"[blue]Calculando {n}! [/]", end="")

c = n
f = 1

while c > 0:
    print(f"{c}", end="")

    if c > 1:
        print(" [green]x[/] ", end="")
    else:
        print(" = ", end="")

    f *= c
    c -= 1

print(f)

n2 = int(input('Digite outro numero para ver seu fatorial: '))
f2 = 1
print(f"[blue]Calculando[/] {n2}! ", end="")

for c2 in range(n2, 0, -1):
    print(c2, end="")

    if c2 > 1:
        print(" [green]x[/] ", end="")
    else:
        print(" = ", end="")

    f2 *= c2

print(f2)
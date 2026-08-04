'''
Crie um programa que leia vários numeros e mostre a soma deles quando o usuário digirar [999]
'''
from rich import print

n = int(input('Digite o número [999 para parar]: '))

soma = 0
cont = 0
while n != 999:
    cont +=1
    soma += n
    n = int(input('Digite o número [999 para parar]: '))

print(f"[green]você digitou [blue]{cont} números[/] e a soma entre eles foi [blue]{soma}[/][/]")
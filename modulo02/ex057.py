'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor 
correto..
'''
from rich import print# biblioteca rich está no módulo 4 - POO

sexo = str(input('Digite seu sexo [M/F]: '))

while sexo not in "MFfm":
    print("[red]As informações estão incorretas![/red]")
    sexo = str(input('Digite seu sexo [M/F]'))

print("[blue]informações corretas!\nObrigado![/blue]")
'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

*Seu programa deverá realizar a operação solicitada em cada caso.
'''
from rich import print #biblioteca no módulo 4 - poo
from time import sleep
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo número: '))
sair_programa = False

while sair_programa == False:
    print("[blue]Digite a opção que você deseja![/]")
    print("[1] somar")
    print("[2] multiplicar")
    print("[3] maior")
    print("[4] novos números")
    print("[5] sair do programa")

    op = int(input('opção: '))

    if op == 1:
        print(f"A soma de {n1} + {n2} = {n1 + n2}")
    elif op == 2:
        print(f"{n1} x {n2} = {n1*n2}")
    elif op == 3:
        if n1 > n2:
            print(f"O número {n1} é maior que {n2}")
        else:
            print(f"O número {n2} é maior que {n1}")
    elif op == 4:
        print("[blue]Informe os números novamente:[/]")
        n1 = int(input('Primeiro numero: '))
        n2 = int(input('Segundo número: '))
    elif op == 5:
        sair_programa = True
    else:
        print("[red]Opção incorreta[/]")
        print("[blue]Informe os números novamente:[/]")
        n1 = int(input('Primeiro numero: '))
        n2 = int(input('Segundo número: '))
        
    print(10 * "=-=")
    sleep(2)

print("[blue]Fim do programa![/]")
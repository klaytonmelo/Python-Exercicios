"""
Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso, de zero até vinte.

Seu programa deverá ler o número pelo teclado(entre 0, 20)
e mostralo por extenso
"""
from rich import print

extenso = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

while True:
    n = int(input('Digite um numero entre 0 e 20: '))

    while n not in range(0, 21):
        print("[red]Tente novamente...[/]")
        n = int(input('Digite um numero entre 0 e 20: '))

    print("[blue]-[/]" * 30)
    print(f"Você digitou o número [green]{extenso[n]}[/]")
    print("[blue]-[/]" * 30)

    op = str(input('Quer continuar ?: '))

    """while op.strip().upper()[0] not in "SN":
        print("[red]ERRO! tente novamente[/]")
        op = str(input('Quer continuar ?: '))"""

    while True:
        if op.strip().upper()[0] not in "SN":
            print("[red]ERRO! tente novamente[/]")
            op = str(input('Quer continuar ?: '))
        else:
            break

    if op.strip().upper()[0] == "N":
        break

print("[blue]Programa finalizado![/]")
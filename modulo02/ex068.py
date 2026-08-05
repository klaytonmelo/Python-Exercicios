"""
faça um programa que jogue par ou impar com o computador. 
O jogo só será interrompido quando o jogador PERDER, mostrando o total
de vitórias consecutivas que ele conquistou no final do jogo!
"""
from random import randint
from rich import print

print("[yellow]-=[/]" * 20)
print("[green]Vamos jogar PAR ou IMPAR[/]")
print("[yellow]-=[/]" * 20)
vitoria = 0
while True:
    jogador = int(input('Diga um valor: '))
    p_i = str(input('Par ou Impar? [P/I]: '))

    while p_i.strip().upper()[0] not in ["P", "I"]:
        print("[red]ERRO![/] [green]digite novamente...[/]")
        p_i = str(input('Par ou Impar? [P/I]: '))

    if p_i.upper() in ["P","PAR"]:
        p_i = "PAR"
    elif p_i.upper() in ["I","IMPAR"]:
        p_i = "IMPAR"

    computador = randint(0, 100)

    soma = computador + jogador
    if soma % 2 == 0:
        op = "PAR"
    else:
        op = "IMPAR"

    print(f"você jogou {jogador} e o [yellow]computador jogou {computador}[/]. Total: {soma} [blue]Resultado: {op}[/]")

    if op == p_i:
        print("[yellow]-=[/]" * 20)
        print("[blue]Você venceu![/]")
        print("[yellow]Vamos jogar novamente...[/]")
        print("[yellow]-=[/]" * 20)
        vitoria += 1
    else:
        break

print("[red]GAME OVER![/]")
print(f"[blue]Você venceu {vitoria} vezes![/]")
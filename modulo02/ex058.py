'''
Melhore o jogo do desafio 028 onde o computador vai "pensar" em 
um número inteiro entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites foram
nescessários para vencer.
'''
from random import randint
from time import sleep
from rich import print # biblioteca no modulo 4 - POO

computador = randint(0,5) #faz o computador "PENSAR"

print("-=-" * 20)
print("[blue]vou pensar em um numero entre 0 e 5, tente adivinhar...[/]")
print("-=-" * 20)

jogador = int(input('Em que número eu pensei? '))
print("[green]processando...[/]")
sleep(3)

palpites = 0
while jogador != computador:
    palpites += 1
    print("[red]Você errou!! tente novamente![/]")
    jogador = int(input('Em que número eu pensei? '))
    print("[green]processando...[green]")
    sleep(2)

print("[blue]Parabéns você acertou!!![/]")
print(15*"[black]-=[/]")
print(f"foram nescessarios {palpites} palpites para você vencer!")
print(15*"[black]-=[/]")
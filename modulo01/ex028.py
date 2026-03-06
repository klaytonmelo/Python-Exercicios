from random import randint
from time import sleep
computador = randint(0,5) #faz o computador "PENSAR"
print("-=-" * 20)
print("vou pensar em um numero entre 0 e 5, tente adivinhar...")
print("-=-" * 20)
jogador = int(input("Em que numero eu pensei ? \n"))#O jogador tenta adivinhar
print("Processando...")
sleep(5)
if jogador == computador:
    print("Parabens! Você conseguiu me vencer")
else:
    print(f"Eu pensei no número {computador} e não no {jogador}")

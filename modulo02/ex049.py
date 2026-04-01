'''
Refaça o DESAFIO 009, mostrando a tabuada de um numero
que o usuário escolher, só que agora utilizando um laço for.
'''
from time import sleep

n = int(input("Digite um numero para ver sua tabuada:\n"))

for c in range(1,11):
    print(f"{n} X {c} = {n*c}")
    sleep(1)
    
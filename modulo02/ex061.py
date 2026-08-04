'''
Refaça o desafio 051, lendo o primeiro termo e a razão de uma
PA, mostrando os 10 primeiros termos da progressão usando a
estrutura while.
'''

print(40 * '=')
print(" Gerador de PA ")
print(40 * '=')

pt = int(input('Primeiro termo: '))
rasao = int(input('Rasão: '))

termo = pt
cont = 1
while cont <= 10:
    print(f"{termo} -> ", end="")
    termo += rasao
    cont += 1

print("Fim")

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
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f"{termo} -> ", end="")
        termo += rasao
        cont += 1

    print("Pausa")

    mais = int(input('Quantos termos você quer mostrar a mais? '))

print("Fim")
print(f"progressão finalizada com {total} termos mostrados")
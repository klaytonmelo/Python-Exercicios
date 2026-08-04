'''
Melhore o desafil 061, perguntando para o
usuário se ele quer mostrar mais alguns
termos. O programa encerra quando ele
disser que quer mostrar 0 termos.
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
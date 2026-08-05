"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No inicio, perguntando ao usuário qual será o valor a ser sacado (numeros inteiros)
e o programa vai informar quantas cédulas de cada valor serão entregues
"""

print("=" * 30)
print(f"{'BANCO CEV':^30}")
print("=" * 30)

valor = int(input('Que valor você quer sacar ? R$'))
total = valor
cedula = 50
tot_ced = 0
while True:
    if total >= cedula:
        total -= cedula
        tot_ced += 1
    else:
        if tot_ced > 0:
            print(f"total de {tot_ced} cédulas de R${cedula}")

        if cedula == 50: 
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        tot_ced = 0

        if total == 0:
            break

print("=" * 30)
print("Volte sempre ao BANCO CEV! tenha um bom dia!")
        
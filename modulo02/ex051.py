'''
Desenvolva um programa que leia o primeiro termo
e a razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão.
'''
print(40 * '=')
print("   10 termos de uma PA")
print(40 * '=')

pt = int(input('Primeiro termo: '))
rasao = int(input('Rasão: '))
decimo = pt + (10 - 1) * rasao

for c in range(pt, decimo + rasao, rasao):
    print(f"{c} →")

print("Acabou")
""" 
Crie um programa que leia varios números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar 999, que é a 
condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flog)
"""

soma = 0
cont = 0

while True:
    n = int(input('Digite um valor [999 para parar]: '))

    if n == 999:
        break

    cont += 1
    soma += n

print(f"você digitou {cont} numeros e a soma entre eles foi {soma}")
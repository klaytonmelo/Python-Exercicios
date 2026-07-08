"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:

>A média de idade do grupo.     --   >Quantas mulheres tem menos de 20 anos.
>Qual é o nome do homem mais velho.
"""

tot_idade = 0
totm_menor20 = 0
maior_idade_homem = 0
n_homem_mais_velho = ""

for c in range(1, 5):
    print(f"---- {c}° pessoa ----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("idade: "))
    sexo = str(input("Sexo [M/F]: "))
    tot_idade += idade

    if c == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        n_homem_mais_velho = nome
    elif sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        n_homem_mais_velho = nome

    if sexo in "Ff" and idade < 20:
        totm_menor20 += 1

media_idade = tot_idade / 4
print(f"A média de idade do grupo é de {media_idade} anos!")
print(f"O homem mais velho tem {maior_idade_homem} anos e se chama {n_homem_mais_velho}!")
print(f"Ao todo são {totm_menor20} mulheres com menos de 20 anos!")
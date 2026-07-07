#Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lido.

maior_peso = 0
menor_peso = 0

for c in range(1, 6):
    peso = float(input(f"peso da {c}° pessoa: "))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso 
        if peso < menor_peso:
            menor_peso = peso
    
print(f"O maior peso lido foi {maior_peso}Kg")
print(f"O menor peso lido foi {menor_peso}Kg")

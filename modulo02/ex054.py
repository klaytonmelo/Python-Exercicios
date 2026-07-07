#Crie um programa que leia o ano de nascimento de 7 pessoas e diga quantas pessos tem maior e menor de idade

from datetime import date
ano_atual = date.today().year

maior = 0
menor = 0

for c in range(1, 8):
    nasc = int(input(f"Em que ano a {c}° pessoa nasceu ? "))
    idade = ano_atual - nasc
    if idade > 18:
        maior += 1
    else:
        menor += 1

print(f"Ao todo tivemos {maior} pessoas maiores de idade.")
print(f"E também tivemos {menor} pessoas menores de idade.")
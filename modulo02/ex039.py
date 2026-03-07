import datetime
from datetime import date
ano_atual = date.today().year
data_n = int(input("Ano de nascimento: "))

idade = ano_atual - data_n

print(f"quem nasceu em {data_n} tem {idade} em {ano_atual}")

if idade == 18:
    print("Você tem que se alistar imediatamete!")
elif(idade < 18):
    print(f"Você ainda não tem 18 anos. Ainda faltam {18 - idade} para o alistamento!")
    print(f"Seu alistamento será em {ano_atual + (18 - idade)}")
else:
    print(f"Você ja deveria ter se alistado a {idade - 18} anos!")
    print(f"seu alistamento foi em {ano_atual - (idade - 18)}")
import datetime
ano_atual = datetime.date.today().year
data_n = int(input("ano de nascimento: "))

idade = ano_atual - data_n

print(f"quem nasceu em {data_n} tem {idade} anos")
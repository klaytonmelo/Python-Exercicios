from datetime import date

a_n = int(input("Qual o seu ano de nascimento?: "))
anos = date.today().year - a_n
print(f"Você tem {anos} anos. ")
ptempo_da = anos - 18
#verifica se a pessoa ja se alistou no serviço militar
alistamento = ''
if anos >=18:
    alistamento = input("você ja se alistou ?")
else:
    print('você terá que se alistar quando fizer 18 anos')

if anos <18 and alistamento == "nâo":
    print("Você terá que se alistar quando fizer 18 anos")
elif anos < 18 and alistamento == "sim":
    print("esta tudo certo! você ja se alistou !")
elif anos == 18 and alistamento == "não":
    print("esta na hora de você se alistar no serviço militar")
elif anos > 18 and alistamento == "não" and ptempo_da == 1:
    print("passou um ano do seu alistamento militar!!")
elif anos > 18 and alistamento == "sim":
    print("esta tudo certo! você ja se alistou !")
else:
    print(f"passou {ptempo_da} anos do seu alistamento militar!!")

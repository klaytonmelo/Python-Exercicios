''' Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
ele vai pagar.

calcule o valor valor da prestação mensal, sabedo que ela não pode
exceder 30% do salario ou então o emprestimo será negado
'''

valor_casa = float(input("Digite o valor da casa? "))
salario = float(input("Digite o valor do seu salário:"))

p_ano = int(input("Em quantos anos deseja pagar :"))

#calculo de porcentagem
pct_limite = salario * 0.30

meses = p_ano * 12

print(salario)
'''p_mes = valor_casa / meses
print(pct_limite)
if p_mes > pct_limite:
    print("Emprestimo negado! \nO valor das parcelas excede 30% de seu salário!")
else:
    print("Emprestimo Confirmado!")'''

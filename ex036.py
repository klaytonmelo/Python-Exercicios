''' Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
ele vai pagar.

calcule o valor valor da prestação mensal, sabedo que ela não pode
exceder 30% do salario ou então o emprestimo será negado
'''

valor_casa = float(input("Digite o valor da casa R$ "))
salario = float(input("Digite o valor do seu salário R$ "))

anos = int(input("Em quantos anos deseja pagar: "))

#calculo de porcentagem
pct_limite = salario * 0.30

prestacao = valor_casa / (anos * 12)

print(f"Para pagar uma casa de R${valor_casa:.2f} em {anos} anos a prestação será de R${prestacao}")

if prestacao > pct_limite:
    print("Emprestimo NEGADO!")
else:
    print("Emprestimo CONCEDIDO!")

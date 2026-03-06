s = float(input('Qual o salário do funcionário? R$'))
p = s * (15/100)
print('o funcionário que ganhava R${}, com 15% de almento, passa a receber R${:.2f}'.format(s,s + p))

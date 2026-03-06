p = float(input('Qual é o preço do produto? R$'))
d = p * (5/100)
print('O produto que custuva {}, na promoção com desconto de 5% vai custar R${:.2f}'.format(p, p - d))

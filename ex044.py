p = float(input("Digite o preço do produto:R$"))

print("formas de pagamento")
print("(1) - à vista: dinheiro/cheque")#10% de desconto
print("(2) - à vista no cartão")#5% de desconto
print("(3) - Em até 2x no cartão")#preço normal
print("(4) - 3x ou mais no cartão")#20% de juros

fp = int(input("Digite a opção corespondente a forma de pagamento:\n"))
if fp == 1:
    desconto = p - (p * 0.10)
    print("seu desconto é de 10%")
    print(f"O produto que custava R${p} ficou R${desconto}")
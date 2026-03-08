print("====== Lojas python ======")
p = float(input("Digite o preço das compras: "))

print("===== FORMAS DE PAGAMENTO =====")
print("[ 1 ] à vista dinhairo/cheque")
print("[ 2 ] à vista cartão")
print("[ 3 ] 2x no cartão")
print("[ 4 ] 3x ou mais no cartão")

op = int(input("escolha a opção: "))

if op == 1:
    total = p - (p * 0.10)
    print(f"Sua compra de R$: {p} vai custar R$: {total} no final.")
elif op == 2:
    total = p - (p * 0.05)  
    print(f"Sua compra de R$: {p} vai custar R$: {total} no final.")
elif op == 3:
    total = p
    parcela = total / 2
    print(f"Sua compmpra será parcelada em 2X de R$: {parcela:.2f} SEM JUROS")  
    print(f"Sua compra de R$: {p} vai custar R$: {total} no final.")
elif op == 4:
    total = p + (p * 0.20)
    tp = int(input("Quantas parcelas: "))
    parcela = total / tp
    print(f"Sua compmpra será parcelada em {tp}X de R$: {parcela:.2f} COM JUROS") 
    print(f"Sua compra de R$: {p} vai custar R$: {total} no final.")
else:
    print("ERRO - tente novamente!")
    print("Opção de pagamento INVALIDA!")
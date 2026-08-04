sair = False
soma = 0
cont = 0
maior = 0
menor = 0

while sair == False:
    n = int(input('Digite um numero: '))
    soma += n
    cont +=1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n >= maior:
            maior = n
        if n <= menor:
            menor = n

    op = str(input('Quer continuar ? [S/N]'))
    if op.upper() == "N":
        sair = True

print(f"Você digitou {cont} números e a média entre eles foi {soma/cont}")
print(f"O maior valor digitado foi {maior} e o menor foi {menor}")
from rich import print

print("[blue]-[/]" * 30)
print("      LOJA SUPER BARATÃO")
print("[blue]-[/]" * 30)

soma = quant_mil = menor_preço = 0
p_mais_barato = ""
cont = 0
while True:
    nome_produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: '))
    cont += 1

    soma += preco

    if preco > 1000:
        quant_mil += 1

    if cont == 1:
        p_mais_barato = nome_produto
        menor_preço = preco
    else:
        if preco <= menor_preço:
            menor_preço = preco
            p_mais_barato = nome_produto

    op = str(input('Quer continuar? [s/n] '))
    while op.strip().upper()[0] not in "SN":
        print("[red]ERRO![/] [green]tente novamente...[/]")
        op = str(input('Quer continuar ? [s/n] '))

    if op.strip().upper()[0] == "N":
        break

print("[blue]-[/]" * 30)
print(f"O total da compra foi R$: {soma:,.2f}")
print(f"Temos {quant_mil} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {p_mais_barato} que custou R${menor_preço:,.2f}")
print("[blue]-[/]" * 30)

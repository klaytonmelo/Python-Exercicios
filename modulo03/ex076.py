"""
Crie um programa que tenha uma tupla única com 
nomes de produtos e seus respectivos preços,
na sequência.

No final, mostre uma listagem de preços, organizando
os dados em forma tabular
"""
from rich import print

produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro" , 34.90)

'''for p in range(0, len(produtos), 2):
    print(f"{produtos[p]:.<30} R$: {produtos[p + 1]:.2f}")'''

print("[green]-[/]" * 30)
print(f"{"[blue]LISTAGEM DE PREÇOS:":^30}[/]")
print("[green]-[/]" * 30)

for p in range(0, len(produtos)):
    if p % 2 == 0:   
        print(f"{produtos[p]:.<30}", end="")
    else:
        print(f"R$: {produtos[p]:>.2f}")
print("[green]-[/]" * 30)
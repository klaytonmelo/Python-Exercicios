"""
Faça um programa que leia vários números, um de cada vez, para cada
valor digitado pelo usuário. o programa será interrompido quando
o numero soliciatado for negativo
"""
from rich import print

while True:
    print("[blue]===== tabuada =====[/]")
    
    n = int(input('numero: '))
    if n < 0:
            break
    
    for c in range(0, 10):
        print(f"{n} x {c} = {n*c}")

print(f"[green]Programa encerrado![/]")

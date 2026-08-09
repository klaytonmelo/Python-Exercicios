"""
Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais
"""
from rich import print

palavras = ("aprender", "programar", "linguagem", "python", "curso", "gratis", "estudar", "praticar", "trabalhar", "mercado", "programador", "futuro")

for p in palavras:
    print(f"\nA palavra [blue]{p.upper()}[/] tem as [yellow]vogais:[/] ", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(f"[green]{letra}[/] ", end="")


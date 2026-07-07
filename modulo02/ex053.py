'''
Crie um programa que leia uma frase
qualquer e diga se ela é um palindromo,
desconsiderando os espaços.

***********
palidromo é aquela frase que da de ler de traz pra frente
e de frente pra trás que vai dar a mesma coisa.

ex: APOS A SOPA
    A SACADA DA CASA
    A TORRE DA DERROTA
    O LOBO AMA O BOLO
    ANOTARAM A DATA DA MARATONA

***********
'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print(f"Você digitou a frase {junto}")

inverso = ""
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print("Temos um palídromo")
else:
    print("A frase digitada não é um palídromo!")
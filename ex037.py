from weakref import finalize

print("escolha a base de conversão:")
print("(1) - binario")
print("(2) - octal")
print("(3) - hexadecimal")

nconv = int(input("Digite o numero de conversão: "))
if nconv == 1 or nconv == 2 or nconv == 3:
    n = int(input("Digíte um número inteiro: "))
else:
    print("Erro!!!, não existe conversão com esse numero!!")

binário = bin(n)
octal = oct(n)
hexadecimal = hex(n)

if nconv == 1:
    print(f"O numero {n} é {binário} em binário")
elif nconv == 2:
    print(f"O numero {n} é {octal} em octal")
elif nconv == 3:
    print(f"O numero {n} é {hexadecimal} em hexadecimal")

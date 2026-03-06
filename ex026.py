#perguntar uma frase
#tranforma em maiuscula e retira os espaços:

#entrada
frase = str(input("digite uma frase: ")).upper().strip()
#saida
print(f"A letra A aparece {frase.count("A")} veses na frase")
print(f"A primeira letra A apareceu na posição: {frase.find("A") + 1}")
print(f"a ultima letra A apareceu na posição :{frase.rfind("A") + 1}")

import random

jop = random.randint(0,2)

while True:
    print("Suas opções")
    print("[0] PEDRA")
    print("[1] PAPEL")
    print("[2] TESOURA")

    op = int(input("Qual é a sua jogada? "))

    #O COMPUTADOR JOGOU
    if jop == 0:
        opcomp = "PEDRA"
    elif jop == 1:
        opcomp = "PAPEL"
    elif jop == 2:
        opcomp = "TESOURA"

    if op == 0 or op == 1 or op == 2:
        #JOGADOR
        if op == 0:
            opjog = "PEDRA"
        elif op == 1:
            opjog = "PAPEL"
        elif op == 2:
            opjog = "TESOURA"

        print("JO \n KEN \n   PO!!!")

        print("-="*10)
        print(f"O computador jogou {opcomp}\nJogador jogou {opjog}")
        print("-="*10)

        if opjog == "PAPEL" and opcomp == "PAPEL" or opjog == "PEDRA" and opcomp == "PEDRA" or opjog == "TESOURA" and opcomp == "TESOURA":
            print("EMPATE!")
        elif opjog == "PEDRA" and opcomp == "PAPEL":
            print("Computador GANHOU!")
        elif opcomp == "PEDRA" and opjog == "PAPEL":
            print("Jogador GANHOU!")
        elif opjog == "PAPEL" and opcomp == "TESOURA":
            print("Computador GANHOU!")
        elif opcomp == "PAPEL" and opjog == "TESOURA":
            print("Jogador GANHOU!")
        elif opjog == "TESOURA" and opcomp == "PEDRA":
            print("Computador GANHOU!")
        elif opcomp == "TESOURA" and opjog == "PEDRA":
            print("JOgador GANHOU!")
        else:
            print("alguem ganhou! OU o Código se recusa a ajudar!!")

        print("="*20)
        print("Deseja jogar de novo?")
        jdn = str(input("Sim (S) ou Não(N):"))
        print("=+="*10)
        if jdn == "S":
            print("Tenha uma boa partida!!")
        else:
            print("Seu jogo minhas regras!\nJOGUE DE NOVO!!!")
            print("Tenha uma boa partida!")
        print("=+="*10)
    else:
        print("Jogo INVALIDO\nJogador PERDEU!!\nTente NOVAMENTE!!!")
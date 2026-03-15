#Crie um programa que faça o computador jogar jokenpô (pedra, papel, tesoura)

import random
from time import sleep
import os


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

itens = ("Pedra", "Papel", "Tesoura")

while True:
    limpar()
    comp = random.randint(0,2)
    
    print("Suas opções")
    print("[0] PEDRA")
    print("[1] PAPEL")
    print("[2] TESOURA")

    try:
        player = int(input("Digite um número: "))
    except ValueError:
        print("Erro! Digite apenas números.")
        while ValueError:
            try:
                player = int(input("Digite um número: "))
                break
            except ValueError:
                print("Erro! Digite apenas números.")
    if player == 0 or player == 1 or player == 2:

        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PO!!!")
        limpar()
        print("-="*10)
        print(f"O computador jogou {itens[comp]}\nJogador jogou {itens[player]}")
        print("-="*10)

        if comp == 0:
            if player == 0:
                print("EMPATE")
            elif player == 1:
                print("Jogador GANHOU!")
            elif player == 2:
                print("Computador GANHOU!")
            else:
                print("erro")
        elif comp == 1:
            if player == 0:
                print("Computador GANHOU!")
            elif player == 1:
                print("EMPATE!")
            elif player == 2:
                print("Jogador GANHOU!")  
            else:
                print("erro")  
        elif comp == 2:
            if player == 0:
                print("Jogador GANHOU!")
            elif player == 1:
                print("Computador GANHOU!")
            elif player == 2:
                print("EMPATE!")
            else:
                print("erro")
        else:
            print("alguem ganhou! OU o Código se recusa a ajudar!!")

        print("="*20)

        sleep(2)
        print("Deseja jogar de novo?")
        sleep(1)
        jdn = str(input("Sim (S) ou Não(N):"))

        print("=+="*10)
        limpar()

        #pergunta se o jogador deseja jogar denovo!
        if jdn.upper() in ["S", "SIM"]:
            print("Tenha uma boa partida!!")
            sleep(3)
        elif jdn.upper() in ["N", "NÃO", "NAO"]:
            print("Seu jogo minhas regras!\nJOGUE DE NOVO!!!")
            print("Tenha uma boa partida!")
            sleep(3)
        else:
            print("ERRO!")
            sleep(3)
        print("=+="*10)
    elif str(player) == "":
        print("Jogo INVALIDO")
        sleep(1)
        print("Jogador PERDEU!!")
        print("Tente NOVAMENTE!!!")
        sleep(2)
    else:
        print("Jogo INVALIDO")
        sleep(1)
        print("Jogador PERDEU!!")
        print("Tente NOVAMENTE!!!")
        sleep(2)

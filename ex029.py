"""v = int(input("Qual a velocidade atual do carro?\n "))
if v > 80:
    multa = (v - 80) * 7
    print(F"Você foi mutado pague R$:{multa}")
else:
    print("voce esta seguindo as regras de transito!! ")"""

velocidade = float(input("Qual a velocidade atual do carro? \n"))
if velocidade > 80:
    print("MULTADO! Você excedeu o limite permitido que é 80km/h")
    multa = (velocidade - 80) * 7
    print(f"Você deve pagar uma multa de R${multa:.2f}")
print("Tenha um bom dia! dirija com segurança!")
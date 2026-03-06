'''dis = float(input("Qual é a distância de sua viagem ? "))
print(f"Você eesta prestes a começar uma viagem de {dis}km.")
if dis <= 200:
    preço = dis * 0.50
else:
    preço = dis * 0.45
print(f"E o preço de sua viagem será de R${preço:.2f}")'''

dis = float(input("Qual é a distância de sua viagem ? "))
print(f"Você eesta prestes a começar uma viagem de {dis}km.")
preço = dis * 0.50 if dis <= 200 else dis * 0.45
print(f"E o preço de sua viagem será de R${preço:.2f}")
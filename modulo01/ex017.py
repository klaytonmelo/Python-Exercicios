from  math import hypot
co = float(input('Qual o comprimento do cateto oposto:'))
ca = float(input('Qual o comprimento do cateto adjacente:'))
hp = hypot(co, ca)
print(f'A hipotenusa vai medir:{hp:.2f}')

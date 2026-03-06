from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(angulo))
print(f'O angulo de {angulo} tem o seno {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'O ângulo de {angulo} tem o cosseno de {cosseno:.2f}')
tangente = tan(radians(angulo))
print(f'O angulo de {angulo} tem a tangente de {tangente:.2f}')

l = float(input('Largura da parede?:'))
a = float(input('Altura da parede?:'))
ar = l*a
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(l, a, ar))
print('para pintar sua parede, você precisará de: {}l de tinta'.format(ar/2))

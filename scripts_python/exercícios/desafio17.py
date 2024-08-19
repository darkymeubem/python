import math
print('=' * 30)
print('Teorema de Pitágoras')
print('=' * 30)
cato = int(input('Informe o valor do cateto oposto:'))
cata = int(input('Informe o valor do cateto adjacente:'))
hip = math.sqrt(cato**2 + cata **2)
print(f'O valor da hipotenusa é {hip:.2f}')
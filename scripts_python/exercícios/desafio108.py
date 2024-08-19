from ex108 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {p} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumenta(p,10))} ')
print(f'Reduzindo 12%, temos {moeda.moeda(moeda.reduz(p,12))}')
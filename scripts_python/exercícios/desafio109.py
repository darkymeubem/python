from ex109 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${moeda.moeda(p)} é R${moeda.metade(p,True)}')
print(f'O dobro de R${moeda.moeda(p)} é {moeda.dobro(p,True)}')
print(f'Aumentando 10%, temos R${moeda.aumenta(p,10,True)} ')
print(f'Reduzindo 12%, temos R${moeda.reduz(p,12,True)}')
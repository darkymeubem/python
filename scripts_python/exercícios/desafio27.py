nome = input('Digite seu nome:').title().strip()
nd = nome.split()
print(f'Prazer em te conheçer {nome} ')
print(f'Seu primeiro nome é {nd[0]} e seu último nome é {nd[-1]}')
dados = []

for p in range (0,2):
    peso = float(input(f'Digite o peso da {p+1}ª pessoa: '))
    dados.append(peso)
print(dados)
print(f'')
print(f'A pessoa com maior peso tem {max(dados)}kg.')
print(f'A pessoa com menor peso tem {min(dados)}kg.')
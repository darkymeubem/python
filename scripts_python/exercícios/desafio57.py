sexo = str(input('Digite seu sexo: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, digite corretamente por favor. ')).upper().strip()
print(f'Sexo {sexo}')
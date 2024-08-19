lista = []
resposta = 'S'
while resposta == 'S':
    valores = int(input('Digite um número: '))
    resposta = str(input('Deseja continuar? [S/N]')).upper().strip()
    if valores not in lista:
        print('Valor adicionado com sucesso.')
        lista.append(valores)
    else:
        print('Valor duplicado, removendo...')
print(lista)
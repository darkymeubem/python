resposta = ''
preco = 0
lista = []
total = 0
soma = 0
precom = 0
maisbarato = ''
while True:
    while resposta != 'N':
        nomep = str(input('Qual o nome do produto? ')).strip().capitalize()
        preco = int(input('Quanto custa o produto? '))
        resposta = str(input('Você quer continua? [S/N]')).upper()
        total = total + preco
        lista.append(preco)
        if preco > 1000:
            soma = soma + 1
        if preco == min(lista):
            maisbarato = nomep
    break
print(f'Você gastou no total R${total}\n{soma} produtos custam mais que R$1000,00\nO produto mais barato é {maisbarato} e custa R${min(lista)} ')
print('{:-^40}'.format('FIM DO PROGRAMA'))
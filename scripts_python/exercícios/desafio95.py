from time import sleep
dados = {'nome': '','gols':'' ,'total': ''}
lista = []
c = 0
a = 0
soma = 0
dados['nome'] = str(input('\033[1mNome do \033[m\033[1;31mJogador\033[m\033[1m:\033[m ')).capitalize().strip()
d = int(input(f'\033[1mQuantas partidas\033[m \033[1;31m{dados["nome"]}\033[m \033[1mjogou?\033[m '))
while c < d:
    c = c + 1
    dados['gols'] = int(input(f'\033[1mQuantos\033[m \033[1;32mgols\033[m \033[1mna partida\033[m \033[1;35m{c}\033[m\033[1m?\033[m '))
    lista.append(dados['gols'])

for c in range(0,len(lista)):
    soma = lista[c] + soma

media = soma/len(lista)

dados['total'] = soma
while a < d:
    print(f'     \033[1m=>Na partida\033[m \033[1;34m{a+1}\033[m\033[1m,\033[m \033[1;31m{dados["nome"]}\033[m \033[1mfez\033[m \033[1;35m{lista[a]}\033[m')
    a = a + 1
    sleep(.5)

print(f'O jogador {dados["nome"]} jogou {d} partidas. ')
print(f'\033[1mTotal de gols\033[m \033[1;31m{dados["total"]}\033[m')
print(f'\033[1mMédia p/ partida:\033[m\033[1;36m{media:.1f}\033[m')

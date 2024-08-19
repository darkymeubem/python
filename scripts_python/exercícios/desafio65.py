print('\033[35m=\033[m\033[34m-\033[m'*30)
print('\033[1;35mMAIOR E MENOR VALORES\033[m')
print('\033[35m=\033[m\033[34m-\033[m'*30)
n = 'S'
s = 0
num = 0
soma = 0
media = 0
lista = []
while n == 'S':
    num = int(input('\033[1;36mDigite um número:\033[m'))
    n = str(input('\033[1mVocê quer continuar? [\033[m\033[1;34mS\033[m\033[1m/\033[m\033[1;31mN\033[m\033[1m]')).strip().upper()
    s = s + 1
    soma = soma + num
    media = soma/s
    lista.append(num)
print(f'\033[1;37mForam\033[m \033[1;32m{s}\033[m \033[1;37mnúmeros digitados, a média é igual a\033[m \033[1;32m{media:.0f}\033[m,\033[1;37m o maior número é\033[m \033[1;32m{max(lista)}\033[m \033[1;37me o menor número é\033[m \033[1;32m{min(lista)}')

"""
'r' -> usado somente para ler algo
'w' -> usado somente para escrever
'r+' -> usado para ler e escrever algo
'a' -> usado para acrescentar ou algo
"""
#Programa Principal
nomes = ['Felipe Pedroza',
'Ricardo Nunes',
'Gustavo Guanabara',
'Maria Luiza Cardoso',
'Fernando Días',
'Maicon Kuster',
'John F. Kennedy']
idade = [16,
25,
37,
15,
19,
23,
65]
lista = []

from ex115 import menu
menu.menup('MENU PRINCIPAL')
with open('names.txt','w') as arquivo:
    for c in nomes:
        arquivo.write(f'{str(c)}\n')
        nomes.append(c)
with open('age.txt','w') as arquivo:
    for c in idade:
        arquivo.write(f'{str(c)}\n')
        idade.append(c)


while True:
    try:
        print(f'\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m\n\033[33m2\033[m - \033[34mCadastrar '
              f'nova pessoa\033[m\n\033[33m3\033[m - \033[34mSair do sistema\033[m')
        n = int(input('Sua opção: '))


    except:
        print('Por favor, digite um valor válido!')

    else:
        if n == 1:
            for c in range(0,len(nomes)):
                for d in range(0,len(idade)):
                    print(f'{nomes[c]} {idade[d]}\n')
        if n == 2:
            try:
                a = str(input('Nome: '))
                b = int(input('Idade: '))


            except ValueError:
                print('\033[31mERROR, Valor inválido!\033[m')

            except TypeError:
                print('\033[31mERROR, Valor inválido!\033[m')


            else:
                with open('name.txt', 'a') as acresc_1:
                    arquivo.write(f'{str(a)}')


                with open('age.txt', 'a') as acresc_2:
                    arquivo.write(f'{str(b)}')


        if n == 3:
            print('Saindo do sistema...')
            break


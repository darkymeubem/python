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
nomes_1 = []
idade_1 = []




arquivo_1 = open("names.txt",'r')
arquivo_2 = open("age.txt",'r')


for d in arquivo_1:
    nomes_1.append(str(d).strip())

for e in arquivo_2:
    idade_1.append(str(e).strip())




from ex115 import menu
menu.menup('MENU PRINCIPAL',15)



while True:

    try:
        print(f'\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m\n\033[33m2\033[m - \033[34mCadastrar '
              f'nova pessoa\033[m\n\033[33m3\033[m - \033[34mSair do sistema\033[m')
        n = int(input('Sua opção: '))


    except:
        print('Por favor, digite um valor válido!')

    else:
        if n == 1:
            menu.linha()
            for c in range(0, len(nomes_1)):
                menu.design(nomes_1[c],idade_1[c])
            menu.menup('MENU PRINCIPAL',15)


        if n == 2:
            menu.menup('NOVO CADASTRO',15)
            while True:
                a = input('Nome: ').strip()
                c = str(a.replace(' ',''))
                if c.isalpha() == True:
                    break


                else:
                    print('\033[31mERRO, Valor inválido!\033[m')

            while True:
                b = input('Idade: ')
                if b.isnumeric() == True:
                    with open('age.txt', 'a') as acresc_2:
                        acresc_2.write(f'{str(b)}\n')
                        idade_1.append(b)

                    with open('names.txt', 'a') as acresc_1:
                        acresc_1.write(f'{str(a)}\n')
                        nomes_1.append(a)
                    break


                else:
                    print('\033[31mERRO, Valor inválido!\033[m')
            menu.menup('MENU PRINCIPAL',15)
        if n == 3:
            menu.linha()
            print('\033[36mSaindo do sistema...\033[m')
            menu.linha()
            break

def beleza( ):
    p =  (input("Palavra: "))
    print(10*'='+ len(p)*'=' + 10*'=')
    print(str(10*" "+p+10*" ").upper())
    print(10*'='+ len(p)*'=' + 10*'=')



from time import sleep

senha = ['senha']
c = 0
while True:
    login = input('\nDigite a senha: ')
    c = c + 1
    if login == senha[0]:
        break


    elif c == 3:
        print('\nAguarde 5 segundos para tentar novamente')
        sleep(5)
        c = 0


    else:
        print('\033[1;31mTente novamente\033[m')

print('Dados: {xxxxxxxxxxx}')


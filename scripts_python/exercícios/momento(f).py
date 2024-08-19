def leiaint(n):
    while True:
        escreva = input(n).strip()
        if escreva.isnumeric() == True:
            print('é número, tá dboa')
            return escreva
            break

        else:
            print('tente novamente. ')


n = leiaint('Digite um número: ')

print(f'Você acabou de digitar {n}')
def leiaint(n):
    while True:
        try:
            escreva = int(input(n).strip())

        except (ValueError, TypeError):
            print('ERROR, Valor inválido!')
            continue

        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pela usuário.')
            break

        else:
            return escreva
            break
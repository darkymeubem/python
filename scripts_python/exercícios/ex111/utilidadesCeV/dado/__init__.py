

def leiadinheiro(msg):
    while True:
        entrada = str(input(msg).replace(',','.').strip())
        if entrada.isnumeric() == True and entrada != '' :
            return entrada
            break

        else:
            print(f'ERROR: "{entrada}" não é um valor válido!')
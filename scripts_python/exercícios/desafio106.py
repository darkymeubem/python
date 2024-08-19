from time import sleep
def work(msg):
    print((len(msg) + 4) * '\033[1m=\033[m')
    print(f'  \033[1m{msg}\033[m  ')
    print((len(msg) + 4) * '\033[1m=\033[m')
while True:
    work('SISTEMA DE AJUDA PyHELP')
    ajuda = input('\033[1mFunção ou Biblioteca: \033[m').strip().lower()
    if ajuda != 'fim':
        print('Ajustando os comandos...')
        sleep(.5)
        print(f'\033[1m{help(ajuda)}\033[m')
    if ajuda == "fim":
        print('\n')
        work('Até logo Jovem Padawan!')
        break

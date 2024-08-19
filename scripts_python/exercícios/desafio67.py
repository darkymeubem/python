print('\033[34m=\033[m\033[36m-\033[m' * 30)
print('\033[1;31mTABUADA v3.0.1\033[m')
print('\033[34m=\033[m\033[36m-\033[m' * 30)
c = 0
n = 0
print('*Para finalizar o programa basta digitar um número negativo*')
while True:
    print('=' *40)
    n = int(input('Digite um número: '))
    print('=' *40)
    c = 0
    if n < 0:
        break
    while c < 10:
        c = c + 1
        print(f'{n} x {c} = {n * c}')

print('\033[34mPROGRAMA FINALIZADO\033[m')

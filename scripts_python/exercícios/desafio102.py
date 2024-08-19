def fatorial(num = 1,show = False):
    f = 1
    print('=' * 30)
    if show == True:
        for c in range(num, 0, -1):
            f = f * c
            print(c,end=' ')
            if c > 1:
                print('x', end=' ')
        print(f'= {f}')


    else:
        for c in range(num,0,-1):
            f = f * c
        print(f'O fatorial de {num} é {f}')
#Programa Principal
fatorial(5, show = True)


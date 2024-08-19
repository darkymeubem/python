from math import sqrt
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
d = (b * b) -4*(a)*(c)
print(d)
def work(msg):
    print((len(msg) + 4) * '\033[1m=\033[m')
    print(f'  \033[1m{msg}\033[m  ')
    print((len(msg) + 4) * '\033[1m=\033[m')
if d < 0:
    print('A equação em questão não tem raízes reais.\n')
    work('Estudo de Sinal')
    if a > 0:
        print('Para todo valor real de x, f(x) vai ser positivo.')
    else:
        print('Para todo valor real de x, f(x) vai ser negativo')

elif d > 0:
    print('Esta equação possuí duas raízes reais.\n')
    x1 = (-b + sqrt(d))/(2*a)
    x2 = (-b - sqrt(d)) / (2*a)
    work('Estudo de sinal')
    if a > 0:
        print(f'f(x) = 0, x = {x1} ou x = {x2}')
        if x1 > 0 and x2 < 0:
            print(f'f(x) > 0, x > {x1} ou x < {x2} ')

        if x1 < 0 and x2 > 0:
            print(f'f(x) > 0, x > {x2} ou x < {x1}')

        if x1 > 0 and x2 > 0  and x1 > x2 :
            print(f'f(x) > 0, x > {x1} ou x < {x2}')

        if x1 > 0 and x2 > 0  and x1 < x2:
            print(f'f(x) > 0, x > {x2} ou x < {x1}')

        if x1 < 0 and x2 < 0 and x1 < x2:
            print(f'f(x) > 0, x > {x2} ou x < {x1}')

        if x1 < 0 and x2 < 0 and x1 > x2:
            print(f'f(x) > 0, x > {x1} ou x < {x2}')

        else :
            if x1 > 0 and  x2 > 0 and x1 > x2:
                print(f'f(x) < 0, S = [x E R/ {x2} < x < {x1}')

            if x1 > 0 and  x2 > 0 and x1 < x2:
                print(f'f(x) < 0, S = [x E R/ {x1} < x < {x2}')

            if x1 < 0 and x2 < 0 and x1 > x2:
                print(f'f(x) < 0, S = [x E R/ {x2} < x < {x1}')

            if x1 < 0 and x2 < 0 and x1 < x2:
                print(f'f(x) < 0, S = [x E R/ {x1} < x < {x2}')







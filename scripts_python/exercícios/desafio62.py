t = int(input('Quantos termos você quer ver?'))
c = 0
if t != 0:
    while c != t:
        if t != 0:
            c = c + 1
            a1 = int(input('Digite o valor do a1:'))
            r = int(input('Qual o valor da razão? '))
            print(f'a{c} = {a1 + (c * r) - r}'  )


import colorama
colorama.init()
print(colorama.Style.BRIGHT,'TABUADA 2.0')
t = int(input('Digite um número:'))
for c in range (0,11):
    print(f'{t} x {c} = {c * t}')
print('FIM')
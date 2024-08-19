km = int(input('Informe a distância da viagem:'))
if km <= 200:
    ct = km * 0.5
    print(f'O custo da viagem será de R${ct:.2f}')

if km >= 200:
    c = km * 0.45
    print(f'O cuto da viagem será de R${c:.2f}')
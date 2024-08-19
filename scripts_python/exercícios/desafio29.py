print('=' * 18)
print('RADAR ELETRÔNICO')
print('=' * 18)

v = int(input('Informe a velocidade do veículo:'))
if v > 80:
    m = (v-80) * 7
    print(f'Seu veículo passou do limite da velocidade permitida da via, você terá que pagar uma multa de R${m} ')
else:
    print('Você passou dentre os limites da velocidade, Continue Assim!!!!!')
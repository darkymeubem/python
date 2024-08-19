print('=' * 40)
print(' E M P R É S T I M O  B A N C Á R I O')
print('=' * 40)
casa = float(input('Qual o valor da casa?'))
sal = float(input('Qual o seu salário atual?'))
ano = float(input('Em quantos anos você pretende pagar?'))
ds = sal * 0.3
m = ano * 12
pm = casa / m
if pm <= ds :
    print(f'O valor da parcela mensal será de R${pm:.2f} e está dentre os limites do empréstimo.')
if pm > ds:
    print(f'Seu empréstimo de parcela R${pm:.2f} foi negado ,pois, estrapola os limites estabelecidos pela nossa empresa que é 30% do seu salário que é de R${ds}')




ano = 2020
cont = 0
s = 0
for c in range(0,7):
    n =int(input('Informe sua data de nascimento:'))
    idade = 2020 - n
    if idade < 18:
        cont = cont + 1
    else:
        s = s + 1
print(f'Das {c+1} pessoas digitadas, {s} são maior de idade e ',end ='')
print(f'{cont} são menor de idade')

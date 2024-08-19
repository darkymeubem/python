h = float(input('Qual a sua altura em metros?'))
p = float(input('Qual é o seu peso em quilogramas?'))
imc = p/(h**2)
print(f'Seu imc é {imc:.2f} e sua classificação é:')
if imc <= 18.5:
    print('ABAIXO DO PESO')
if imc > 18.5 and imc <= 25:
    print('PESO IDEAL')
if imc > 25 and imc <= 30:
    print('SOBREPESO')
if imc > 30 and imc <= 40:
    print('OBESIDADE')
if imc > 40:
    print('OBESIDADE MÓRBIDA')
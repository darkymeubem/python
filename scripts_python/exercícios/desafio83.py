lista = []
valores = str(input('Digite uma expressão: '))
lista.append(valores)
if '(' in valores[0] and ')' in valores[-1]:
    if (lista.count('(') - lista.count(')')) == 0 or (lista.count(')') - lista.count('(')) == 0 :
        print('A sua expressão é válida')

else:
    print('A sua expressão é inválida!!!')

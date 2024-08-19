valor = float(input('Informe o valor do produto, R$'))
pag = str(input('Qual sua forma de pagamento?\nDentre as formas de pagamento estão: \nCrédito \nDébito \nDinheiro \nCheque\nÀ vista\n===============\n')).lower()
if pag == 'dinheiro' or pag == 'cheque':
    print(f'Seu produto terá 10% de desconto, seu valor final a pagar será de R${valor - (valor * 0.1)}')
if pag == 'cartão de crédito' or pag =='crédito' or pag == 'cartao de credito' or pag == 'credito':
    cart = input('O senhor pode dividir em:\n2x no cartão  \n3x no cartão \nQual a sua escolha? (Por favor escreva apenas o número):')
    if cart =='2':
        print(f'Seu pagamento não terá juros e nem desconto, o valor da parcela mensal será de R${valor/2 } ')
    if cart == '3':
        print(f'Seu pagamento terá um juros de 20%, o valor da parcela mensal será de R${(valor + (valor *0.2))/3:.2f}\n O valor final a pagar é R${valor + (valor *0.2)} e o valor original era de R${valor}')
if pag == 'a vista' or pag == 'à vista' or pag == 'débito' or pag == 'debito':
    print(f'Seu pagamento terá 5% de desconto, o valor final a pagar será de R${valor - (valor * 0.05)}')
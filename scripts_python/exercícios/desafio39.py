import colorama
colorama.init()
print(colorama.Style.BRIGHT,'=' * 40)
print('Alistamento Obrigatório ao Exército')
print('=' * 40)
ano = int(input('Informe seu ano de nascimento:'))
idade = 2020 - ano
if idade < 18:
    print(f'Você ainda não pode se alistar ou participar do exército, ainda falta {18 - idade} ano(s) para você entrar.\nSeu alistamento ao exército será em {(18 - idade) + 2020}.')
elif idade > 18:
    print(f'Você estrapulou {idade - 18} ano(s)')
    a = str(input('Você já se alistou ao exército?')).title()
    if a == 'Sim':
        print('OK, Já pode vazar daqui. RALA')
    if a == 'Não' or a == 'Nao':
        print(f'Seu alistamento correto seria no ano de {2020 - (idade - 18)}\n Você é obrigado a se alistar por pelo menos 1 mês')
else:
    print('Seu alistamento será neste ano, 2020.')
    print('Você tem que se alistar neste ano.')
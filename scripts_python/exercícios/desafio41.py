import colorama
colorama.init()
ano = int(input('Qual seu ano de Nascimento?'))
idade = 2020 - ano
if idade <= 9:
    print(colorama.Style.BRIGHT,'CATEGORIA:\n',colorama.Fore.CYAN,' MIRIM  ')
if idade > 9 and idade <= 14:
    print(colorama.Style.BRIGHT,'CATEGORIA:\n',colorama.Fore.BLUE ,'INFANTIL')
if idade > 14 and idade <= 19:
    print(colorama.Style.BRIGHT,'CATEGORIA:\n',colorama.Fore.RED, 'JÚNIOR')
if idade == 20:
    print(colorama.Style.BRIGHT, 'CATEGORIA:\n',colorama.Fore.GREEN,' SÊNIOR')
if idade > 20:
    print(colorama.Style.BRIGHT, 'CATEGORIA:\n MASTER')
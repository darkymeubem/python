dados = {'Nome': '','Ano de nascimento': '', 'Carteira de Trabalho':'' ,'Ano de contratação': '','Salário': ''}
dados['Nome'] = str(input('Digite seu nome: '))
dados['Ano de nascimento'] = int(input('Digite seu ano de nascimento: '))
dados['Carteira de Trabalho'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['Carteira de Trabalho'] == 0:
    print('=' * 50)
    print(f'Nome: {dados["Nome"]}')
    print(f'Idade: {2020 - dados["Ano de nascimento"]}')
    print(f'Ctps: 0')
else:
    dados['Ano de contratação'] = int(input('Digite o seu ano de contratação: '))
    if dados['Ano de contratação'] < dados["Ano de nascimento"]:
        print('Não tem como trabalhar antes de nascer caraio.')
    else:
        dados['Salário'] = int(input('Digite o valor do seu salário: '))
        print('=' * 60)
        print(f'Nome: {dados["Nome"]}')
        print(f'Idade: {2020 - dados["Ano de nascimento"]}')
        print(f'Ctps: {dados["Carteira de Trabalho"]}')
        print(f'Ano de primeira contratação: {dados["Ano de contratação"]}')
        print(f'Salário: R${dados["Salário"]}')
        print(f'Tempo até estar aposentado é de {(dados["Ano de contratação"] + 35) - 2020} anos, você vai se aposentar com {(2020 - dados["Ano de nascimento"]) + (dados["Ano de contratação"] - 1985)} anos, no ano de {dados["Ano de contratação"] + 35}')
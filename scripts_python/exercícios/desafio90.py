dados = {'nome': '', 'média': '','situação': ''}

dados['nome'] = str(input('Qual é o seu nome? '))
dados['média'] = float(input('Qual é a sua média? '))
if dados['média'] < 6:
    dados['situação'] = 'REPROVADO'
else:
    dados['situação'] = 'APROVADO'

print(f'Nome: {dados["nome"]}')
print(f'Média: {dados["média"]}')
print(f'Situação: {dados["situação"]}')




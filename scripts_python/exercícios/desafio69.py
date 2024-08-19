idade = 0
sexo = ''
resposta = ''
maiordeidade = 0
ome = 0
cuie20 = 0
soma = 0
while True:
    while resposta != 'N':
        print('=' * 20)
        print('CADASTRE UMA PESSOA')

        idade = int(input('Digite sua idade: '))
        print('=' * 20)
        sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
        print('=' * 20)
        resposta = str(input('Você quer continuar? [S/N]')).upper()
        soma = soma + 1
        if idade >= 18:
            maiordeidade = maiordeidade + 1
        if sexo == 'M':
            ome = ome + 1
        if sexo == 'F' and idade < 20:
            cuie20 = cuie20 + 1
    break
print(f'Foram {soma} pessoas registradas, dentre elas:\n{maiordeidade} eram maior de idade\n{ome} eram homens\n{cuie20} eram mulheres e tinham menos de 20 anos.')
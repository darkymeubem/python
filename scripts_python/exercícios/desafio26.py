frase = str(input('Digite uma frase qualquer:')).strip().lower()
fd = str(frase.split())
fab= frase.find('a') + 1
a = frase.count('a')
#print(f'A letra "a" aparece {a} vezes')
#print('A letra "a" aparece no primeiro grupo de palavras?')
#print('a' in fd[0])
#print(f'Caso aparecer -1 significa que não aparece \n{fab}')
print('A letra "a" aparece primeiramente na posição: {}'.format(fab))


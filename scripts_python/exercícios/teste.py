print("""Verificador de Palíndromo!!!
Não digite palavras com acento!
Ao escrever a palavra, aperte enter.""")
frase = str(input('Digite a frase para verificar se é um palíndromo: ')).upper().strip()
str_palindromo = frase.replace(' ', '').replace('!', '').replace(',', '').replace('.', '').replace('?', '').replace('É', 'E').replace('Ó', 'O').replace('Á', 'A')
palindromo = bool(True)
for c in range(0, len(str_palindromo)):
    if str_palindromo[c] != str_palindromo[(-c) - 1]:
        palindromo = bool(False)
        break
if palindromo == True:
    print('\033[1;32mA frase É um palíndromo!!!\033[m')
else:
    print('\033[1;31mA frase NÃO É um palíndromo!!!\033[m')
print('Muito obrigado!!!')
lista = ('Lápis','Borracha','Caderno','Livro','Calculadora','Transferidor','Caneta','Compasso','Mochila','Pasta')
listap = (3,1.50,17,50,9.99,15,3.75,11.5,75,11.75)
print('='*44)
print('{:^44}'.format('LISTAGEM DE PREÇOS'))
print('='*44)
for c in range(0,len(lista)):
    print('{}{}R$ {:.2f}'.format(lista[c],'.'* (35-len(lista[c])),listap[c]))
print('='*44)
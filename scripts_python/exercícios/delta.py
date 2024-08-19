a = int(input('Informe o valor de a:'))
b = int(input('Informe o valor de b:'))
c = int(input('Informe o valor de c:'))
delta = b**2 -4*(a)*(c)
if delta < 0:
    print('Não existe raíz')
elif delta == 0:
    print('Existe apenas uma raíz')
else:
    print('Existe duas raízes')
print(f'valor do delta é {delta}')
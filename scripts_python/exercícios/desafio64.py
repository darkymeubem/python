n = 0
s = 0
anterior = 0
posterior = 0
soma = 0

while n != 999:
    n = int(input('Digite um número:'))
    if n != 999:
        soma = soma + n
        s = s + 1
print(f'Você digitou {s-1} até digitar o número correto, a soma dos números digitados foi de {soma} ')

s = 0
n = 0
q = 0
while True:
    n = int(input('Digite um número:'))
    q = q + 1
    if n != 999:
        s = s + n
    if n == 999:
        break

print(f'\033[34;1mForam {q} números digitados, e a soma entre eles é igual a {s}')

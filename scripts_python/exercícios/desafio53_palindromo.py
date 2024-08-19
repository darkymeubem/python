#PALÍNDROMO
a = str(input('Digite uma frase/palavra sem acentuação :')).strip().lower()

d = a.split()
j = ''.join(d)


p1 = a[::-1]
pc = p1.split()
pic = ''.join(pc)

if j == pic:
    print(f'\033[31mA palavra/frase\033[m \033[36m{a}\033[m é um palíndromo, a palavra invertida seria \033[36m{p1}\033[m')
else:
    print(f'\033[36mA palavra/frase\033[m \033[31m{a}\033[m \033[36mnão é um palíndromo!!!\033[m ')



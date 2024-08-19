import random
a = 0
print('=' * 30)
print('    IA      vs      HUMANO')
print('=' * 30)
escolha = int(input('Tente adivinhar um númentro entre 0 e 10 mortal:'))
sd = random.randint(0,10)
while escolha != sd:
    escolha = int(input('Parece que você errou!\n Tente novamente.'))
    a = a + 1
print(f'Seu total de tentativas foi {a} e o número escolhido pela IA foi {sd}')

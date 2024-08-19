import random
print('=' * 30)
print('    IA      vs      HUMANO')
print('=' * 30)
escolha = int(input('Tente adivinhar um númentro entre 0 e 5 mortal:'))
sd = random.randint(0,5)
if escolha == sd:
    print('Parabéns jovem, parece que tenho que treinar muito mais para combater a humanidade, até logo.')
else:
    print('IA VENCE')
print (sd)
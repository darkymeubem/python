import random
print('=-'*20)
print('Par ou Ímpar')
print('=-'*20)
print('REGRAS: \n1- Se você perder você não joga mais\n2- Se você ganhar o jogo continua :)')
sd = random.randint(1,10)
a = 0
ip = ''
s = 0
resposta = ''
while True:
    while ip != 'PERDEU':
        print('='*20)
        a = int(input('Digite um número:'))
        ip = str(input('Par ou Ímpar? [I/P]')).upper()
        s = s + 1
        if (a + sd) % 2 == 0:
            resposta = 'P'
            if ip == resposta:
                print(f'Você jogou {a} e a IA {sd}, totalizando {a + sd} e o número é PAR.')
                print(f'Você venceu, jogue novamente!')
                ip = 'VENCEU'
            else:
                print('Você perdeu :/')
                ip = 'PERDEU'

        if (a + sd) % 2 == 1:
            resposta = 'I'
            if ip == resposta:
                print(f'Você jogou {a} e a IA {sd}, totalizando {a + sd} e o número é ÍMPAR.')
                print(f'Você venceu, jogue novamente!')
                ip = 'VENCEU'
            else:
                print('Você perdeu :/')
                ip = 'PERDEU'
    break
if (s-1) == 1:
    print('='*30)
    print('Você venceu uma vez.\nPrograma finalizado.')
if (s-1) == 0:
    print('='*30)
    print('Você não ganhou nenhuma vez, seu NOOB')
if (s-1) != 0 and (s-1) != 1:
    print('='*30)
    print(f'Você venceu {s-1} vezes\nPrograma Finalizado.')


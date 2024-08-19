def lin():
    print('=' * 65)

def area(comprimento,largura):
    a = comprimento * largura
    lin()
    print(f'A área de seu terreno com as dimensões ({comprimento:.2f},{largura:.2f}) é de: {a:.2f}m^2')


area(float(input('Digite a largura do terreno (m): ')),float(input('Digite o comprimento do terreno (m): ')))

lista = []
homem_velho = []
cuie = 0
macho_vei = 0
for c in range(0,2):
    n = input(f'Digite o nome da {c+1}a pessoa:\n').strip().lower()
    i = float(input(f'Digite a idade da {c+1}a pessoa:\n'))
    s = input(f'\033[1;34mDigite o\033[1;34m \033[1;31msexo\033[m \033[1;34mda {c+1}a pessoa:\033[m\n').strip().lower()
    lista.append(i)
    homem_velho.append(n)

    if s == 'm':
        macho_vei = max(lista)


        print(f'O homem mais velho é {  (n)} com seus {max(lista)} anos')


s = 0
cont = 0
for c in range (0,501):
    if c % 2 == 1:
       if c % 3==0:
           cont = cont + 1
           s = s + c

print(f'A soma de todos os {cont} números ímpares múltiplos por 3 é igual {s} ')
tupla = (str(input('Digite uma frase: ')).lower(),str(input('Digite uma frase: ')).lower(),str(input('Digite uma frase: ')).lower())
a = 0
e = 0
i = 0
o = 0
u = 0
for c in range(0,len(tupla)):
    a = a + tupla[c].count('a')
    e = e + tupla[c].count('e')
    i = i + tupla[c].count('i')
    o = o + tupla[c].count('o')
    u = u + tupla[c].count('u')
s = a + e + i + o + u
print('As palavras',end=' ')
for d in range (0,len(tupla)):
    print(f'{tupla[d]}',end=',')
print(f'possuem {s} vogais')

import random
s1 = random.randint(0,100)
s2 = random.randint(0,100)
s3 = random.randint(0,100)
s4 = random.randint(0,100)
s5 = random.randint(0,100)

tupla = (s1,s2,s3,s4,s5)
print(f'Os valores sorteados foram: {str(tupla)}'.replace(',',' ->').replace('(','').replace(')',''))
print(f'O maior número é {max(tupla)} e o menor é {min(tupla)}')


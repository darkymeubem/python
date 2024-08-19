

#Forma incorreta de atribuir uma variável a um resultado desta função
"""def somar(a = 0, b = 0,c = 0):
    s = a + b + c
    print(f'A soma vale {s}')


resp = somar(3,4,5)
resp1 = somar(9,2)
resp2 = somar(3)

print(f'As somas valem respectivamente: {resp}, {resp1}, {resp2}')"""


#Forma Correta de atribuir uma váriavel a um resultado desta função

def somar(a = 0, b = 0,c = 0):
    s = a + b + c
    return s

resp = somar(3,4,5)
resp1 = somar(9,2)
resp2 = somar(3)

print(f'As somas valem respectivamente: {resp}, {resp1}, {resp2}')


# Desta forma eu consigo formatar a função dentro do programa principal, utilizando o return para retornar o valor de soma (neste caso)
# da função ao programa principal


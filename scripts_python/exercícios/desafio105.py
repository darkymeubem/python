lista = []
dic = {'maior':'','menor':'','média': ''}

def notas(*n):
    s = 0
    for valor in n:
        lista.append(valor)
        s = valor + s
    m = s/len(lista)
    dic['maior'] = max(lista)
    dic['menor'] = min(lista)
    dic['média'] = m
    print('NOTAS DA TURMA: ',end=' ')
    for c in range(0,len(lista)):
        print(lista[c],end=' ')
    print(f'\nA maior nota foi {dic["maior"]} e a menor foi {dic["menor"]}. Média da turma: {dic["média"]:.2f}\nTotal de alunos: {len(lista)}')
    return n

print('=-'*30)
print('DADOS DA TURMA')
print(notas(6,8,2,7))
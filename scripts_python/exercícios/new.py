#Exemplos de funções





"""def beleza(p):
    print(10*'='+ len(p)*'=' + 10*'=')
    print(str(10*" "+ p+10*" ").capitalize())
    print(10*'='+ len(p)*'=' + 10*'=')

beleza("batata")
beleza("SIMMMMM")"""


"""def soma(*n):
    print(n)




soma(1,3,4,5,5)"""


from random import randint

lista = []
for c in range(0,5):
    lista.append(randint(0,100))


def dobra(lst):
    print(lst)
    for c in range(0,len(lst)):
        lst[c] = lst[c] * 2

    print(lst)

dobra(lista)


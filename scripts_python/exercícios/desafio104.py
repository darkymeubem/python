def leiaint(n):
    if n.isnumeric:
        input()
        return n
    else:
        while n not in n.isnumeric:
            return n
n = leiaint('Digite um número: ')
print(leiaint(n))
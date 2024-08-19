nome = input("Qual é o seu nome?")
n1 = int(input("Qual foi sua primeira nota {}?".format(nome)))
n2 = int(input('Qual foi sua segunda nota {}'.format(nome)))
m = (n1 + n2)/ 2
print("A média de {} foi de {}".format(nome,m))
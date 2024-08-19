valores = []
d = 0
for c in range(0,3):
    a = str(input("Qual sua idade?"))
    valores.append(a)
for c in range(0,len(valores)):
    d = d + 1
    print(f"Pessoa {d} tem {valores[c].strip()}")
print("Obrigado por sua participação!")
import math
a = float(input('Digite um ângulo:'))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print(f'O seno do ângulo {a:.0f} é {s:.2f} \n O cosseno é {c:.2f} \n A  tangente é {t:.2f}')
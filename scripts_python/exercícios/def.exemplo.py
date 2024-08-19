def soma(*num):
    s = 0
    for v in num:
        s = v + s
    print(f'{s}')

soma(9,4,5,7,1)

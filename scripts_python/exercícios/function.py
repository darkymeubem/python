def function(b):
    global a
    a = 8
    b = b + 1
    c = 2
    print(f'Agora que A é global (dentro da função) , tanto o de dentro quanto de fora valem o mesmo valor que é \033[1:34m({a})\033[m')
    print(f'O B de dentro vale \033[1:34m({b})\033[m  ')
    print(f'O C de dentro vale \033[1:34m({c})\033[m')

a = 5
print(f'Esse é o valor de A \033[1:34m({a})\033[m antes de eu chamar a função, quando eu chamo a função ele recebe um novo valor')
function(a)
print(f'Como foi chamado a função, agora o valor de A é \033[1:34m({a})\033[m')
p = input(f'{10 *"=":>}pablo{10*"=":<}')
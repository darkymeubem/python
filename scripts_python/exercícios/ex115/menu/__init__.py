
def menup(msg,qntd = 10):
    global tam
    tam = len(f'{qntd*"=":>}{msg}{qntd*"=":<}')
    print(tam*"=")
    print(f'{qntd*" ":>}{msg}{qntd*" ":<}')
    print(tam * "=")
    return tam


def design(nome = '',idade = 0):
    print(f'\033[34m{nome}\033[m{((tam - len(nome) - len(str(idade)) - 5)  * " ")}\033[35m{idade}\033[m anos')

def linha():
    print(tam * "=")


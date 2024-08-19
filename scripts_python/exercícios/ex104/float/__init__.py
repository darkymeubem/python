def leiareal(n):
    while True:
        try:
            escreva = float(input(n).strip())

        except (ValueError, TypeError):
            print('ERROR, Valor inválido!')
            continue

        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pela usuário.')
            break
        else:
            return escreva
            break

nomes = [[['Felipe Pedroza'], [16]],[['Ricardo Nunes'], [24]],[['Gustavo Guanabara'], [37]],[['Maria Luiza Cardoso'],[15]],[['Fernando Días'],[29]]
    ,[['Maicon Kuster'],[19]],[['John F. Kennedy'], [65]]]
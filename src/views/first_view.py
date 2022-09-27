def introduction_page():
    message = '''
        As três calculadoras

        * Primeira Calculadora - 1
        * Segunda Calculadora - 2
        * Terceira Calculadora - 3       
        * Sair - 4
    '''

    print(message)
    command = input('Comando: ')
    return command

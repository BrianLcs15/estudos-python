while True:

    nome = input('Digite seu nome de usuário: ')

    if nome == 'BrianLcs':
        print('Bem vindo, ' + nome)
        break

    if nome != 'BrianLcs':
        print('Usuário inválido. tente novamente')
        continue

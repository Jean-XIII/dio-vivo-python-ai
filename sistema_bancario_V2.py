saldo = 0
LIMITE_SAQUE = 3
lista_deposito = []
lista_saque = []

while True:
    escolha = input(
        'Digite um número para utilizar um dos serviços:\n'
        '1 - Depósito\n'
        '2 - Saque\n'
        '3 - Extrato\n'
        '4 - Sair\n'
        'Sua escolha: '
    )

    if escolha == '1':
        valor_deposito = float(input('Digite o valor do depósito: R$'))

        while valor_deposito <= 0:
            valor_deposito = float(input('Você não pode depositar valores abaixo de 0!\nDigite o valor a ser depositado: R$'))

        saldo += valor_deposito
        lista_deposito.append(valor_deposito)

    elif escolha == '2':
        if LIMITE_SAQUE != 0:
            valor_saque = float(input(
                f'Você pode realizar {LIMITE_SAQUE} de 3 saques diários de no máximo R$ 500,00.\n'
                'Valor a ser sacado: R$'
            ))

            if valor_saque <= 0:
                print('Valor inválido!')
            elif valor_saque > 500:
                print('Você não pode sacar mais que R$500,00!')
            elif valor_saque > saldo:
                print(f'Saldo insuficiente! Você quer sacar R${valor_saque:.2f} mas tem R${saldo:.2f}.')
            else:
                saldo -= valor_saque
                print(f'Você sacou R${valor_saque:.2f}, saldo restante: R${saldo:.2f}')
                lista_saque.append(valor_saque)
                LIMITE_SAQUE -= 1
        else:
            print('Você não pode mais sacar por hoje, tente outro dia!')

    elif escolha == '3':
        print(50 * '=')
        print('Depósitos:')
        for valor in lista_deposito:
            print(f'Depósito realizado no valor de R${valor:.2f}.')

        print(50 * '=')
        print('Saques:')
        for valor in lista_saque:
            print(f'Saque realizado no valor de R${valor:.2f}.')

        print(50 * '=')
        print(f'Saldo Final: R${saldo:.2f}.')

    elif escolha == '4':
        break

    else:
        print('Digite um número válido!')
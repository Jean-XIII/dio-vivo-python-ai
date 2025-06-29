import os

deposito = saque = 0
LIMITE_SAQUE =3
lista_deposito = list()
lista_saque = list()

while True:
    escolha = int(input('Digite um número para utilizar um dos serviços:\n1 - Depósito\n2 - Saque\n3 - Extrato\nSua escolha:'))
    os.system('cls')

    if escolha == 1:
        valor_deposito = float(input('Digite o valor do depósito: R$'))
        while valor_deposito < 1:
            valor_deposito = float(input('Você não pode depositar valores abaixo de 0!\nDigite o valor a ser depositado: R$'))
        deposito += valor_deposito
        lista_deposito.append(valor_deposito)

    elif escolha == 2:
        if LIMITE_SAQUE != 0:
            valor_saque = float(input(f'Você pode realizar {LIMITE_SAQUE} de 3 saques diários de no máximo R$ 500,00.\nValor a ser sacado: R$'))
            if valor_saque > 500:
                print('Você não pode sacar mais que R$500,00!')
            elif valor_saque > deposito:
                print(f'Saldo insuficiente! Você quer sacar R${valor_saque:.2f} mas tem R${deposito:.2f} depositado.')
            else:
                deposito -= valor_saque
                print(f'Você sacou R${valor_saque:.2f}, saldo restante: R${deposito:.2f}')
                lista_saque.append(valor_saque)
                LIMITE_SAQUE -= 1
        else:
            print('Você não pode mais sacar por hoje, tente outro dia!')
        
    elif escolha == 3:
        print(50*'=')
        print('Depósitos:')
        for deposito in lista_deposito:
            print(f'Depósito realizado no valor de R${deposito:.2f}.')
        print(50*'=')
        print('Saques:')
        for saque in lista_saque:
            print(F'Saque realizado no valor de ${saque:.2f}.')
        print(50*'=')
        print(f'Saldo Final: R${deposito:.2f}.')
    else:
        print('Digite um número válido!')

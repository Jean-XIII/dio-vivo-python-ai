def menu():
    return input(
        '\nDigite uma opção:\n'
        '[d] Depósito\n'
        '[s] Saque\n'
        '[e] Extrato\n'
        '[nu] Novo usuário\n'
        '[nc] Nova conta\n'
        '[lc] Listar contas\n'
        '[q] Sair\n'
        '=> '
    )


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f'Depósito: R${valor:.2f}')
        print('Depósito realizado.')
    else:
        print('Valor inválido!')
    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        print('Valor inválido!')
    elif valor > saldo:
        print('Saldo insuficiente!')
    elif valor > limite:
        print('Limite por saque excedido!')
    elif numero_saques >= limite_saques:
        print('Limite de saques atingido!')
    else:
        saldo -= valor
        extrato.append(f'Saque: R${valor:.2f}')
        numero_saques += 1
        print('Saque realizado.')

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print('\n' + '=' * 50)
    if not extrato:
        print('Nenhuma movimentação.')
    else:
        for item in extrato:
            print(item)
    print(f'\nSaldo: R${saldo:.2f}')
    print('=' * 50)


def criar_usuario(usuarios):
    cpf = input('CPF: ')

    for u in usuarios:
        if u['cpf'] == cpf:
            print('Usuário já existe!')
            return

    nome = input('Nome: ')
    usuarios.append({'nome': nome, 'cpf': cpf})
    print('Usuário criado.')


def buscar_usuario(cpf, usuarios):
    for u in usuarios:
        if u['cpf'] == cpf:
            return u
    return None


def criar_conta(contas, usuarios):
    cpf = input('CPF do usuário: ')
    usuario = buscar_usuario(cpf, usuarios)

    if not usuario:
        print('Usuário não encontrado!')
        return

    numero = len(contas) + 1

    conta = {
        'numero': numero,
        'usuario': usuario,
        'saldo': 0,
        'extrato': [],
        'numero_saques': 0
    }

    contas.append(conta)
    print('Conta criada.')


def listar_contas(contas):
    for conta in contas:
        print('=' * 40)
        print(f'Conta: {conta["numero"]}')
        print(f'Titular: {conta["usuario"]["nome"]}')


def selecionar_conta(contas):
    if not contas:
        print('Nenhuma conta cadastrada.')
        return None

    numero = int(input('Número da conta: '))

    for conta in contas:
        if conta['numero'] == numero:
            return conta

    print('Conta não encontrada!')
    return None


def main():
    LIMITE_SAQUES = 3
    LIMITE_VALOR = 500

    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            criar_conta(contas, usuarios)

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao in ['d', 's', 'e']:
            conta = selecionar_conta(contas)
            if not conta:
                continue

            if opcao == 'd':
                valor = float(input('Valor: '))
                conta['saldo'], conta['extrato'] = depositar(
                    conta['saldo'], valor, conta['extrato']
                )

            elif opcao == 's':
                valor = float(input('Valor: '))
                conta['saldo'], conta['extrato'], conta['numero_saques'] = sacar(
                    conta['saldo'],
                    valor,
                    conta['extrato'],
                    LIMITE_VALOR,
                    conta['numero_saques'],
                    LIMITE_SAQUES
                )

            elif opcao == 'e':
                exibir_extrato(conta['saldo'], conta['extrato'])

        elif opcao == 'q':
            break

        else:
            print('Opção inválida!')


main()
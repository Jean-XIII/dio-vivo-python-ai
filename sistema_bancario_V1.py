import os

deposito_tot = saque = 0
LIMITE_SAQUE = 3
historico_saque = list()
historico_deposito = list()

def deposito(valor_deposito):
    while valor_deposito <= 0:
        valor_deposito = float(input('Você não pode depositar valores abaixo de 0! Digite um valor válido: R$'))
    return valor_deposito
        
def saque(valor_saque, arg_limite, arg_deposito):
    if arg_limite > 0:
        if valor_saque > 500:
            return 'Você não pode sacar mais que R$500,00!'
        elif valor_saque > arg_deposito:
            return f'Saldo insuficiente! Você quer sacar R${valor_saque:.2f} mas tem R${arg_deposito:.2f} depositado.'
        else:
            arg_deposito -= valor_saque
            return valor_saque, arg_deposito, arg_limite - 1
    else:
        return 'Você não pode mais sacar por hoje, tente outro dia!'

while True:
    escolha = int(input('Digite um número para utilizar um dos serviços:\n1 - Depósito\n2 - Saque\n3 - Extrato\nSua escolha:'))
    os.system('cls')

    if escolha == 1:
        var_temp = deposito(float(input('Digite o valor do depósito: R$')))
        deposito_tot += var_temp
        historico_deposito.append(var_temp)
        print(f'Você depositou R${var_temp:.2f}')

    elif escolha == 2:
        saq_temp, deposito_tot, LIMITE_SAQUE = saque(valor_saque=float(input(f'Você pode realizar {LIMITE_SAQUE} de 3 saques diários de no máximo R$ 500,00.\nValor a ser sacado: R$')), arg_limite=LIMITE_SAQUE, arg_deposito=deposito_tot)
        print(f'Você sacou R${saq_temp:.2f}, restando R${deposito_tot:.2f} no seu saldo.')

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

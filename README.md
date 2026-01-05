# dio-vivo-python-ai

# Sistema Bancário Simples em Python

Projeto de estudo desenvolvido em Python para praticar lógica de programação, estruturas de controle, listas e interação com o usuário via terminal.

O sistema simula operações bancárias básicas, como depósito, saque e visualização de extrato, seguindo regras simples de negócio.

---

## Objetivo do projeto

Este projeto tem como objetivo praticar conceitos fundamentais de Python, incluindo:

- Estruturas condicionais (`if`, `elif`, `else`)
- Laços de repetição (`while`)
- Manipulação de listas
- Controle de fluxo do programa
- Validação de entrada do usuário
- Simulação de regras de negócio simples

---

## Funcionalidades

- Depósito de valores (somente valores positivos)
- Saque com:
  - Limite máximo de R$ 500,00 por saque
  - Limite diário de 3 saques
  - Verificação de saldo disponível
- Registro de depósitos e saques
- Exibição de extrato com histórico de operações
- Exibição do saldo final

---

## Regras de negócio

- Não é permitido depositar valores menores ou iguais a zero
- Cada saque não pode ultrapassar R$ 500,00
- O usuário pode realizar no máximo 3 saques por execução do programa
- Não é permitido sacar valor maior que o saldo disponível

---

## Como executar o projeto

1. Certifique-se de ter o Python instalado (versão 3.x)
2. Clone o repositório ou copie o arquivo `.py`
3. Execute o programa no terminal:

```bash
python nome_do_arquivo.py
```
Exemplo de uso
Ao executar o programa, será exibido um menu com as opções:
```bash
1 - Depósito
2 - Saque
3 - Extrato
```
O usuário pode realizar depósitos, efetuar saques respeitando as regras e visualizar o extrato das operações realizadas.
Observações

Este projeto foi desenvolvido exclusivamente para fins de estudo e aprendizado em Python.
Não possui persistência de dados (as informações são perdidas ao encerrar o programa) e não representa um sistema bancário real.

# Simulador de Operações Bancárias

## Descrição

Este projeto é um simulador de operações bancárias desenvolvido em Python, utilizando conceitos de Programação Orientada a Objetos (POO). O objetivo principal é praticar e demonstrar habilidades em POO, além de criar uma aplicação funcional que simula operações bancárias básicas. O projeto é executado via terminal, onde o usuário pode selecionar opções para realizar diversas operações bancárias.

## Funcionalidades

- **Abrir Conta**: Permite ao usuário abrir diferentes tipos de contas (Corrente, Investimento, Salário, Estudantil).
- **Acessar Conta**: Permite ao usuário acessar uma conta existente e realizar operações como verificar saldo, fazer depósito, saque e transferência.
- **Visualizar Todas as Contas**: Exibe os dados de todas as contas criadas.
- **Sair**: Encerra o programa.

## Tipos de Contas

- **Conta Corrente**: Conta com saldo inicial, limite de cheque especial e possibilidade de empréstimo.
- **Conta de Investimento**: Conta com saldo inicial mínimo de R\$5000, destinada a investimentos.
- **Conta Salário**: Conta destinada ao recebimento de salário, sem possibilidade de transferências ou empréstimos.
- **Conta Estudantil**: Conta destinada a estudantes com idade entre 16 e 25 anos, com possibilidade de empréstimo.

## Estrutura do Projeto

- **abrir_conta.py**: Contém a função `abrir_conta` responsável por coletar dados do usuário e criar diferentes tipos de contas.
- **painel_de_controle.py**: Contém a função `exibir_menu` que exibe o menu principal do programa.
- **acessar_conta.py**: Contém a função `acessar_conta` que permite ao usuário acessar uma conta existente e realizar operações.
- **Conta.py**: Define a classe base `Conta` com métodos para depósito, saque, transferência e solicitação de empréstimo.
- **Conta_corrente.py**: Define a classe `ContaCorrente` que herda de `Conta` e adiciona funcionalidades específicas para contas correntes.
- **Conta_investimento.py**: Define a classe `ContaInvestimento` que herda de `Conta` e adiciona funcionalidades específicas para contas de investimento.
- **Conta_salario.py**: Define a classe `ContaSalario` que herda de `Conta` e adiciona funcionalidades específicas para contas salário.
- **Conta_estudantil.py**: Define a classe `ContaEstudantil` que herda de `Conta` e adiciona funcionalidades específicas para contas estudantis.
- **utils.py**: Contém funções utilitárias como `validar_formato_data` e `gerar_numero_conta`.



def acessar_conta(contas):
    numero_conta = input("digite o número da conta: ")
    conta = next((c for c in contas if c.numero == numero_conta), None)
    if conta:
        while True:
            print(f"\n===== Conta {conta.numero} =====")
            print("1. Verificar saldo")
            print("2. Fazer depósito")
            print("3. Fazer saque")
            print("4. Fazer transferência")
            print("5. Voltar ao menu principal")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                print(f"Saldo atual: R$ {conta.saldo:.2f}")
            elif opcao == '2':
                valor = float(input("Digite o valor do depósito: "))

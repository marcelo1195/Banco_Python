
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
            elif opcao == '3':
                valor = float(input("Digite um valor de saque: "))
                conta.sacar(valor)
            elif opcao == '4':
                numero_conta_destino = input("Digite o número da conta de destino: ")
                conta_destino = next((c for c in contas if c.numero == numero_conta_destino), None)
                if conta_destino:
                    valor = float(input("Digite o valor da transferencia: "))
                    conta.transferir(valor, conta_destino)
                else:
                    print('Conta de destino não encontrada.')
            elif opcao == '5':
                break
            else:
                print("Opção inválida. tente novamente.")
    else:
        print('Conta não encontrada. ')
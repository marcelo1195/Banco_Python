from abrir_conta import  abrir_conta
from acessar_conta import acessar_conta
from painel_de_controle import exibir_menu

# Variavel de controle para calcular os numeros das contas
proximo_numero_conta = 000

contas = []

def main():
    while True:
        opcao = exibir_menu()
        if opcao == '1':
            nova_conta = abrir_conta()
            if nova_conta:
                contas.append(nova_conta)
        elif opcao == '2':
            acessar_conta(contas)
        elif opcao == '3':
            for conta in contas:
                print(conta)
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opcao invalida. tente novamente.")

if __name__ == '__main__':
    main()
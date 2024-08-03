from datetime import datetime
import utils
from pessoa import Pessoa
from conta.Conta_corrente import ContaCorrente
from conta.Conta_investimento import ContaInvestimento
from conta.Conta_salario import ContaSalario
from conta.Conta_estudantil import ContaEstudantil
from utils import validar_formato_data


#validador de data de nascimento
def abrir_conta():
    while True:
        nome = input("Digite seu nome: ")
        sobrenome = input("Digite seu sobrenome: ")
        data_nascimento = validar_formato_data()
        cpf = input("Difite seu cpf: ")
        idade = utils.calcular_idade(datetime.strptime(data_nascimento, "%d/%m/%Y"))

        print("\nOs dados estão corretos ?")
        print(f"nome: {nome}, sobrenome: {sobrenome}, cpf: {cpf}, data de nascimento: {data_nascimento}, idade: {idade} anos")
        correto = (input("(S/N): ").upper())
        if correto == "S":
            break
        else:
            continue

    #instanciando um objeto pessoa
    pessoa = Pessoa(nome, sobrenome, data_nascimento, cpf)
    idade = pessoa.idade()

    # gerando o npumero de conta e agencia
    numero_conta = str(hash(cpf))[:8]
    agencia = "0001"

    while True:
        print("\nQual tipo de conta deseja abrir ?")
        print("Digite 1 para abrir conta corrente")
        print("Digite 2 para abrir conta de investimento")
        print("Digite 3 para abrir conta salario")
        print("digite 4 para abrir conta estudantil")
        print("digite 0 para sair\n")

        tipo_conta = input("conta tipo: ")

        if tipo_conta == "0":
            break

        elif tipo_conta == "1":
            saldo_inicial = float(input("Digite o saldo inicial: "))
            emprestimo = 2500
            limite_cheque_especial = 500
            conta = ContaCorrente(pessoa, numero_conta, agencia, saldo_inicial, emprestimo, tipo=1, limite_cheque_especial=limite_cheque_especial)
            print("Cota corrente criada com sucesso !")


        elif tipo_conta == "2":
            saldo_inicial = float(input("Digite o investimento inicial (minimo R$5000): "))
            if saldo_inicial < 5000:
                print("Saldo inicial insuficiente para abrir uma conta de investimento")
                continue
            else:
                conta = ContaInvestimento(pessoa, numero_conta, agencia, saldo_inicial)
                print("Conta de investimento criada com sucesso !")

        elif tipo_conta == "3":
            saldo_inicial = 0
            conta = ContaSalario(pessoa, numero_conta, agencia, saldo_inicial)
            print("Conta salario criada com sucesso !")

        elif tipo_conta == "4":
            if idade <16 or idade >25:
                print("Idade não permitida para uma conta estudantil.")
                continue
            saldo_inicial = float(input("Digite o saldo inicial: "))
            conta = ContaEstudantil(pessoa, numero_conta, agencia, saldo_inicial, emprestimo=0)
            print("Conta estudantil criada com sucesso !")

        else:
            print("Tipo de conta inválido, Tente novamente \n")
            continue

        #imprimindo informações da conta
        print("\nInformações da conta:")
        print(f"Titular: {conta.titular.nome} {conta.titular.sobrenome}")
        print(f"Número da conta: {conta.numero}")
        print(f"Agência: {conta.agencia}")
        print(f"Tipo de conta: {tipo_conta}")
        print(f"Saldo: R$ {conta.saldo:.2f}")
        if hasattr(conta, 'limite_cheque_especial'):
            print(f"Limite de cheque especial: R$ {conta.limite_cheque_especial:.2f}")
        if hasattr(conta, 'emprestimo'):
            print(f"Limite de empréstimo: R$ {conta.emprestimo:.2f}")

        break


if __name__ == '__main__':
    abrir_conta()
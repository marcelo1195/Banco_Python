from datetime import datetime
import utils
from pessoa import Pessoa
from conta.Conta_corrente import ContaCorrente
from conta.Conta_investimento import ContaInvestimento
from conta.Conta_salario import ContaSalario
from conta.Conta_estudantil import ContaEstudantil
from conta.Conta import Conta
def abrir_conta():
    while True:
        nome = input("Digite seu nome: ")
        sobrenome = input("Digite seu sobrenome: ")
        data_nascimento = datetime.strptime(input("Digite sua data de nascimento no formato DD/MM/YYYY: "), "%d/%m/%Y")
        cpf = input("Difite seu cpf: ")

        idade = utils.calcular_idade(data_nascimento)

        print("Os dados estão corretos ?")
        print(f"nome: {nome}, sobrenome: {sobrenome}, cpf: {cpf}, data de nascimento: {data_nascimento}, idade: {idade} anos")
        correto = input("(S/N)")
        if correto == "S":
            return False
        else:
            return True


    #instanciando um objeto pessoa
    pessoa = Pessoa(nome, sobrenome, data_nascimento, cpf)
    idade = pessoa.idade()

    # gerando o npumero de conta e agencia
    numero_conta = str(hash(cpf))[:8]
    agencia = "0001"

    while True:
        print("Qal tipo de conta deseja abrir ?")
        print("Digite 1 para abrir conta corrente")
        print("Digite 2 para abrir conta de investimento")
        print("Digite 3 para abrir conta salario")
        print("digite 4 para abrir conta estudantil")
        print("digite 0 para sair")

        tipo_conta = input("conta tipo: ")

        if tipo_conta == "0":
            break

        # Criando objetos Conta

        elif tipo_conta == "1":
            saldo_inicial = float(input("Digite o saldo inicial: "))
            emprestimo = 2500
            limite_cheque_especial = 500
            conta = ContaCorrente(pessoa, numero_conta, agencia, saldo_inicial, emprestimo, tipo=1, limite_cheque_especial=limite_cheque_especial)

        elif tipo_conta == "2":
            saldo_inicial = float(input("Digite o investimento inicial (minimo R$5000): "))
            if saldo_inicial < 5000:
                print("Saldo inicial insuficiente para abrir uma conta de investimento")
                return
            else:
                conta = ContaInvestimento(pessoa, numero_conta, agencia, saldo_inicial)

        elif tipo_conta == "3":
            saldo_inicial = 0
            conta = ContaSalario(pessoa, numero_conta, agencia, saldo_inicial, tipo_conta=3)

        elif tipo_conta == "4":
            if idade <16 or idade >25:
                print("Idade não permitida para uma conta estudantil.")
                return
            saldo_inicial = float(input("Digite o saldo inicial: "))
            conta = ContaEstudantil(pessoa, numero_conta, agencia, saldo_inicial, emprestimo=0)

        else:
            print("Tipo de conta inválido.")
            print(conta)

from conta import Conta

class ContaSalario(Conta):
    def __init__(self, titular, numero, agencia, saldo):
        super().__init__(titular, numero, agencia, saldo, tipo=4,)

    def receber_salario(self, quantia):
        self.depositar(quantia)
        print(f"Salario de R${quantia} recebido. Saldo atual: R${self.saldo}")

    def transferir(self, quantia, conta_destino):
        print("Transferências não são permitidas para contas salário.")

    def solicitar_emprestimo(self, quantia):
        print("Empréstimos não são permitidos para contas salário.")
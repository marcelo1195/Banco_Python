from conta import Conta

class ContaEstudantil(Conta):
    def __init__(self, titular, numero, agencia, saldo, emprestimo = 0):
        super().__init__(titular, numero, agencia, saldo, tipo=4, emprestimo = emprestimo)
    def tipo_de_conta(self, tipo):
        return "Estudantil"


from conta.Conta import Conta

class ContaInvestimento(Conta):
    def __init__(self, titular, numero, agencia, saldo):
        super().__init__(titular, numero, agencia, saldo, tipo=2, emprestimo=(saldo*5))
    def investir(self, quantia):
        if quantia <= self.saldo:
            print(f"Investimento de R${quantia} realizado com sucesso. saldo atual de: R$:{self.saldo}")
        else:
            print("Saldo insuficiente para investimentos")
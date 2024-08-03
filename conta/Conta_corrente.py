from conta.Conta import Conta
class ContaCorrente(Conta):
    def __init__(self, titular, numero, agencia, saldo, emprestimo, tipo = 1 , limite_cheque_especial = 500):
        if saldo <= 0:
            raise ValueError("O saldo inicial da conta corrente não pode ser zero ou negativo")
        super().__init__(titular, numero, agencia, saldo, emprestimo, tipo)
        self.limite_cheque_especial = limite_cheque_especial

    def sacar(self, quantia):
        if quantia <= self.saldo + self.limite_cheque_especial:
            self.saldo -= quantia
            print(f"Saque de R${quantia} realizado com sucesso. Saldo atual: R${self.saldo}")
        else:
            print("Limite de cheque especial excedido")

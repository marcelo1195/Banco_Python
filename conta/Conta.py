from utils import calcular_idade
from pessoa import Pessoa

class Conta:
    def __init__(self, titular, numero, agencia, saldo, tipo=0, emprestimo=0):
        self._titular = titular
        self._numero = numero
        self._agencia = agencia
        self._saldo = float(saldo)
        self._tipo = int(tipo)
        self._emprestimo = float(emprestimo)

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        if not isinstance(titular, Pessoa):
            raise ValueError("Titular deve ser uma instância da classe Pessoa.")
        self._titular = titular

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, agencia):
        self._agencia = agencia

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = float(saldo)

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = int(tipo)

    @property
    def emprestimo(self):
        return self._emprestimo

    @emprestimo.setter
    def emprestimo(self, emprestimo):
        self._emprestimo = float(emprestimo)

    def depositar(self, quantia):
        self.saldo += quantia
        print(f"Depósito de R${quantia} realizado com sucesso. Saldo atual: R${self.saldo}")

    def sacar(self, quantia):
        if quantia <= self.saldo:
            self.saldo -= quantia
            print(f"Saque de R${quantia} realizado com sucesso. Saldo atual: R${self.saldo}")
        else:
            print("Saldo insuficiente.")

    def transferir(self, quantia, conta_destino):
        if quantia <= self.saldo:
            conta_destino.depositar(quantia)
            self.saldo -= quantia
            print(
                f"Transferência de R${quantia} efetuada com sucesso para a conta {conta_destino.numero} de titular {conta_destino.titular.nome} {conta_destino.titular.sobrenome}.")
        else:
            print("Saldo insuficiente.")

    def solicitar_emprestimo(self, quantia):
        if self.tipo == 3 or self.tipo == 4:
            print("Conta não autorizada a efetuar empréstimo.")
        else:
            self.emprestimo += quantia
            self.saldo += quantia
            print(f"Empréstimo de R${quantia} concedido. Saldo atual: R${self.saldo}")

    def __str__(self):
        return f"Titular: {self.titular.nome} {self.titular.sobrenome}, Número: {self.numero}, Agência: {self.agencia}, Saldo: R${self.saldo}, Tipo: {self.tipo}, Empréstimo: R${self.emprestimo}"
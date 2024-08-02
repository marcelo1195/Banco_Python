from utils import calcular_idade
from pessoa import *

class Conta:
    def __init__(self, titular, numero, agencia, saldo=0, tipo=0, emprestimo=0):
        self.titular = titular
        self.numero = numero
        self.agencia = agencia
        self.saldo = float(saldo)
        self.tipo = int(tipo)
        self.emprestimo = float(emprestimo)


    def depositar(self, quantia):
        self.saldo += quantia
        print(f"deposito de R${quantia} realizado com sucesso. Saldo atual: {self.saldo}")

    def sacar(self, quantia):
        if quantia <= self.saldo:
            self.saldo -= quantia
            print(f"Saque de {quantia} realizado com sucesso. Saldo atual de {self.saldo}")
        else:
            print("saldo insuficiente.")

    def transferir(self, quantia, conta_destino):
        if quantia <= self.saldo:
            conta_destino.depositar(quantia)
            self.saldo -= quantia
            print(f"Transferencia efetuada com sucesso para conta: {conta_destino.numero} de titular {conta_destino.titular.nome} {conta_destino.sobrenome}")
        else:
            print("Saldo insuficiente")

    def solicitar_emprestimo (self, quantia):
        if self.tipo == 2 or self.tipo==3:
            print("Conta não autirozada a efetuar emprestimo")
        else:
            self.emprestimo += quantia
            self.saldo = self.saldo + quantia
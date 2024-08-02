from datetime import datetime
from utils import calcular_idade


class Pessoa:
    def __init__(self, nome, sobrenome, data_nascimento, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self._sobrenome = sobrenome

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self._data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    def __str__(self):
        return f"Nome: {self._nome}, Sobrenome: {self._sobrenome}, data de nascimento: {self._data_nascimento}, CPF: {self._cpf} "

    def idade(self):
        return calcular_idade(self._data_nascimento)

from .mdl_endereco import Endereco
from .mdl_contato import Contato
from .mdl_credenciais import Credenciais


class Usuario:
    def __init__(self, nome: str, cpf: str, rg: str, nascimento: str, genero: str,
                 endereco: Endereco, contato: Contato):
        self._nome = nome
        self._cpf = cpf
        self._rg = rg
        self._nascimento = nascimento
        self._genero = genero
        self._endereco = endereco.get_endereco()
        self._contato = contato.get_contato()

        self._credenciais = Credenciais()

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value: str):
        self._nome = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value: str):
        self._cpf = value

    @property
    def rg(self):
        return self._rg

    @rg.setter
    def rg(self, value: str):
        self._rg = value

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, value: str):
        self._nascimento = value

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, value: str):
        self._genero = value

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, value: Endereco):
        self._endereco = value

    @property
    def contato(self):
        return self._contato

    @contato.setter
    def contato(self, value: Contato):
        self._contato = value

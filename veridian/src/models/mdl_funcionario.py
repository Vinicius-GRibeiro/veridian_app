from .mdl_usuario import *


class Medico(Usuario):
    def __init__(self, nome: str, cpf: str, rg: str, nascimento: str, genero: str, endereco: Endereco, contato: Contato,
                 cargo: str):

        super().__init__(nome, cpf, rg, nascimento, genero, endereco, contato)

        self._cargo = cargo

    def __str__(self):
        return self.get_funcionario()

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, value: str):
        self._cargo = value

    def get_funcionario(self):
        return {
            'nome': self.nome,
            'cpf': self.cpf,
            'rg': self.rg,
            'nascimento': self.nascimento,
            'genero': self.genero,
            'endereco': self.endereco,
            'contato': self.contato,
            'cargo': self.cargo
        }

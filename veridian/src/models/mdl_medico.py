from .mdl_usuario import *


class Medico(Usuario):
    def __init__(self, nome: str, cpf: str, rg: str, nascimento: str, genero: str, endereco: Endereco, contato: Contato,
                 crm: str, especialidade: str):

        super().__init__(nome, cpf, rg, nascimento, genero, endereco, contato)

        self._crm = crm
        self._especialidade = especialidade

    def __str__(self):
        return self.get_medico()

    @property
    def crm(self):
        return self._crm

    @crm.setter
    def crm(self, value: str):
        self._crm = value

    @property
    def especialidade(self):
        return self.especialidade

    @especialidade.setter
    def especialidade(self, value: str):
        self._especialidade = value

    def get_medico(self):
        return {
            'nome': self.nome,
            'cpf': self.cpf,
            'rg': self.rg,
            'nascimento': self.nascimento,
            'genero': self.genero,
            'endereco': self.endereco,
            'contato': self.contato,
            'crm': self.crm,
            'especialidade': self.especialidade
        }

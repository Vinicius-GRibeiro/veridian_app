from .mdl_usuario import *


class Paciente(Usuario):
    def __init__(self, nome: str, cpf: str, rg: str, nascimento: str, genero: str, endereco: Endereco, contato: Contato,
                 fator_rh: str, convenio: str, alergias: list[str] = None):

        super().__init__(nome, cpf, rg, nascimento, genero, endereco, contato)

        self._fator_rh = fator_rh
        self._alergias = alergias
        self._convenio = convenio

    def __str__(self):
        return self.get_paciente()

    @property
    def fator_rh(self):
        return self._fator_rh

    @fator_rh.setter
    def fator_rh(self, value: str):
        self._fator_rh = value

    @property
    def alergias(self):
        return self._alergias

    @alergias.setter
    def alergias(self, value: str):
        self._alergias = value

    @property
    def convenio(self):
        return self._convenio

    @convenio.setter
    def convenio(self, value: str):
        self._convenio = value

    def get_paciente(self):
        return {
            'nome': self.nome,
            'cpf': self.cpf,
            'rg': self.rg,
            'nascimento': self.nascimento,
            'genero': self.genero,
            'endereco': self.endereco,
            'contato': self.contato,
            'rh': self.fator_rh,
            'alergias': self.alergias,
            'convenio': self.convenio
        }



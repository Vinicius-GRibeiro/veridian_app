class Endereco:
    def __init__(self, cep: str, rua: str, numero: str, bairro: str, cidade: str, estado: str, complemento: str = None):
        self._cep = cep
        self._rua = rua
        self._numero = numero
        self._bairro = bairro
        self._cidade = cidade
        self._estado = estado
        self._complemento = complemento

    def __str__(self):
        return self.get_endereco()

    @property
    def cep(self):
        return self._cep

    @cep.setter
    def cep(self, value):
        self._cep = value

    @property
    def rua(self):
        return self._rua

    @rua.setter
    def rua(self, value):
        self._rua = value

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        self._numero = value

    @property
    def bairro(self):
        return self._bairro

    @bairro.setter
    def bairro(self, value):
        self._bairro = value

    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, value):
        self._cidade = value

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value):
        self._estado = value

    @property
    def complemento(self):
        return self._complemento

    @complemento.setter
    def complemento(self, value):
        self._complemento = value

    def get_endereco(self) -> dict:
        return {
            'cep': self.cep,
            'rua': self.rua,
            'numero': self.numero,
            'bairro': self.bairro,
            'cidade': self.cidade,
            'estado': self.estado,
            'complemento': self.complemento
        }
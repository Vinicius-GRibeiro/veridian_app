class Credenciais:
    def __init__(self, login: str = None, senha: str = None):
        self._login = login
        self._senha = senha
        self._logado = False

    def __str__(self):
        return self.get_credenciais()

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value: str):
        self._login = value

    @property
    def senha(self):
        if self._logado:
            return self._senha
        return

    @senha.setter
    def senha(self, value: str):
        if self._logado:
            self._senha = value
            return
        return

    @property
    def logado(self):
        return self._logado

    @logado.setter
    def logado(self, value: bool):
        self._logado = value

    def get_credenciais(self):
        if self.logado:
            return {
                'cod': 0,
                'login': self.login,
                'senha': self.senha
            }
        return {
            'cod': -1
        }

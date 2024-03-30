class Contato:
    def __init__(self, cel1: str, email: str, cel2: str = None):
        self._cel1 = cel1
        self._cel2 = cel2
        self._email = email

    def __str__(self):
        return self.get_contato()

    @property
    def cel1(self):
        return self._cel1

    @cel1.setter
    def cel1(self, value):
        self._cel1 = value

    @property
    def cel2(self):
        return self._cel2

    @cel2.setter
    def cel2(self, value):
        self._cel2 = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    def get_contato(self) -> dict:
        return {
            'cel1': self.cel1,
            'cel2': self.cel2,
            'email': self.email
        }

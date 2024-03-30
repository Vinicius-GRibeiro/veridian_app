from _conexao import Conexao
from usuarios import Usuario

db = Conexao()


class Paciente:
    @classmethod
    def adicionar(self, rh: str, alergias: str, convenio: str, cpf_usario: str):
        query = '''
            INSERT INTO pacientes (rh, alergias, convenio, cpf_usuario) values (?, ?, ?, ?)
        '''
        dados = (rh, alergias, convenio, cpf_usario)

        db.executar_query(query, dados)

    @classmethod
    def buscar(self, colunas='*', condicao=None):
        query = f'SELECT {colunas} from pacientes'

        if condicao is not None:
            query += f' WHERE {condicao}'

        dados = db.executar_query(query, operacao_de_consulta=True)
        return dados

    @classmethod
    def editar(self, id: int, dicionario_campo_valor):
        campos = ', '.join([f"{campo} = ?" for campo in dicionario_campo_valor.keys()])

        dados = tuple(dicionario_campo_valor.values())
        query = f'UPDATE pacientes SET {campos} WHERE id = {id}'

        db.executar_query(query, dados)

    @classmethod
    def excluir(self, condicao):
        query = f'DELETE FROM pacientes WHERE {condicao}'
        db.executar_query(query)


# rh = ['A+', 'O-', 'AB+', 'AB-']
# alergia = ['', 'frutos do mar', 'dipirona', '']
# convenios = ['CA', 'CB', 'CC', 'CD']
# cpfs = Usuario.buscar(colunas='cpf')[:4:]
#
# for n, item in enumerate(rh):
#     Paciente.adicionar(rh=item, alergias=alergia[n], convenio=convenios[n], cpf_usario=cpfs[n][0])



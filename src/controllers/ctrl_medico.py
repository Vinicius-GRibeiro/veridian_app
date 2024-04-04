from ctrl_conexao import Conexao
from ctrl_usuarios import Usuario

db = Conexao()


class Medico:
    @classmethod
    def adicionar(self, crm: str, especialidade: str, cpf_usuario: str):
        query = '''
            INSERT INTO medicos (crm, especialidade, cpf_usuario) values (?, ?, ?)
        '''
        dados = (crm, especialidade, cpf_usuario,)

        db.executar_query(query, dados)

    @classmethod
    def buscar(self, colunas='*', condicao=None):
        query = f'SELECT {colunas} from medicos'

        if condicao is not None:
            query += f' WHERE {condicao}'

        dados = db.executar_query(query, operacao_de_consulta=True)
        return dados

    @classmethod
    def editar(self, id: int, dicionario_campo_valor):
        campos = ', '.join([f"{campo} = ?" for campo in dicionario_campo_valor.keys()])

        dados = tuple(dicionario_campo_valor.values())
        query = f'UPDATE medicos SET {campos} WHERE id = {id}'

        db.executar_query(query, dados)

    @classmethod
    def excluir(self, condicao):
        query = f'DELETE FROM medicos WHERE {condicao}'
        db.executar_query(query)


if __name__ == '__main__':
    crm = ['1000', '2000', '3000', '4000']
    especialidades = ['cardiologista', 'pediatra', 'fonoaudiólogo', 'ortopedista']
    cpfs = Usuario.buscar(colunas='cpf')[4:8:]

    for n, item in enumerate(crm):
        Medico.adicionar(crm=item, especialidade=especialidades[n], cpf_usuario=cpfs[n][0])

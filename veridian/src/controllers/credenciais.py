from usuarios import Usuario
from contato import Contato
from _conexao import Conexao
from criptografia import gerar_hash

db = Conexao()


class Credencial:
    @classmethod
    def adicionar(cls, login: str, senha: str, cpf: str):
        query = '''
            INSERT INTO credenciais (login, senha, cpf_usuario) values (?, ?, ?)
        '''

        dados = (login, gerar_hash(senha), cpf)

        db.executar_query(query, dados)

    @classmethod
    def buscar(cls, colunas='*', condicao=None):
        query = f'SELECT {colunas} from credenciais'

        if condicao is not None:
            query += f' WHERE {condicao}'

        dados = db.executar_query(query, operacao_de_consulta=True)

    @classmethod
    def editar(cls, id: int, dicionario_campo_valor):
        campos = ', '.join([f"{campo} = ?" for campo in dicionario_campo_valor.keys()])

        dados = tuple(dicionario_campo_valor.values())
        query = f'UPDATE credenciais SET {campos} WHERE id = {id}'

        db.executar_query(query, dados)

    @classmethod
    def excluir(cls, condicao):
        query = f'DELETE FROM credenciais WHERE {condicao}'
        db.executar_query(query)


senhas = ['tLM8U7Un', 'GWrOYrEH', '2Hxh8u8e', 'FjAuw0NO', 'FXwl1Jcj', 'NbMDu8ZS', 'ZGYNRYkt', 'D4c27KyP', 'c270wYcR',
          'eObiYCIU', 'Lw0cJWPR', 'XPMKGFGk']

cpfs = Usuario.buscar(colunas='cpf')
ids_contato = Usuario.buscar(colunas='id_contato')
emails = []

for n, id in enumerate(ids_contato):
    Credencial.adicionar(login=Contato.buscar(colunas='email', condicao=f'id={id[0]}')[0][0],
                         senha=senhas[n], cpf=cpfs[n][0])

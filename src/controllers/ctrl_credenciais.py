from src.controllers.ctrl_conexao import Conexao
from src.controllers.ctrl_criptografia import gerar_hash

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

        query = f"SELECT {colunas} FROM credenciais"

        if condicao is not None:
            query += f" WHERE {condicao}"
        dados = db.executar_query(query, operacao_de_consulta=True)
        dados_ = None
        if dados is not None:
            dados_ = [x[0] for x in dados]

        return dados_

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

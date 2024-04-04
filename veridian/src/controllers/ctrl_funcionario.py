from ctrl_usuarios import Usuario
from ctrl_conexao import Conexao

db = Conexao()


class Funcionario:
    @classmethod
    def adicionar(self, cargo: str, cpf_usurio: str):
        query = '''
            INSERT INTO funcionarios (cargo, cpf_usuario) values (?, ?)
        '''
        dados = (cargo, cpf_usurio)

        db.executar_query(query, dados)

    @classmethod
    def buscar(self, colunas='*', condicao=None):
        query = f'SELECT {colunas} from funcionarios'

        if condicao is not None:
            query += f' WHERE {condicao}'

        dados = db.executar_query(query, operacao_de_consulta=True)
        return dados

    @classmethod
    def editar(self, id: int, dicionario_campo_valor):
        campos = ', '.join([f"{campo} = ?" for campo in dicionario_campo_valor.keys()])

        dados = tuple(dicionario_campo_valor.values())
        query = f'UPDATE funcionarios SET {campos} WHERE id = {id}'

        db.executar_query(query, dados)

    @classmethod
    def excluir(self, condicao):
        query = f'DELETE FROM funcionarios WHERE {condicao}'
        db.executar_query(query)


if __name__ == '__main__':
    cpfs = Usuario.buscar('cpf')[8::]
    cargos = ['recepcionista', 'gerente', 'auxiliar de serviços gerais', 'recepcionista']

    for n, carg in enumerate(cargos):
        Funcionario.adicionar(cargo=carg, cpf_usurio=cpfs[n][0])

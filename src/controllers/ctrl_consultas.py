from src.controllers.ctrl_conexao import Conexao
from src.controllers.ctrl_data_horario import gerar_timestamp


db = Conexao()


class Consulta:
    @classmethod
    def adicionar(cls, cpf_paciente: str, cpf_medico: str, data: str, hora: str):
        query = '''
            INSERT INTO consultas (cpf_paciente, cpf_medico, timestamp)
            VALUES (?, ?, ?)
        '''

        dados = (cpf_paciente, cpf_medico, gerar_timestamp(data, hora))

        db.executar_query(query, dados)

    @classmethod
    def buscar(cls, colunas='*', condicao=None, ordenar_por=None):
        query = f"SELECT {colunas} from consultas"

        if condicao is not None:
            query += f" WHERE {condicao}"

        if ordenar_por is not None:
            query += f" ORDER BY {ordenar_por}"

        dados = db.executar_query(query, operacao_de_consulta=True)

        return dados

    @classmethod
    def editar(cls, id: int, dicionario_campo_valor):
        campos = ', '.join([f"{campo} = ?" for campo in dicionario_campo_valor.keys()])

        dados = tuple(dicionario_campo_valor.values())
        query = f'UPDATE consultas SET {campos} WHERE id = {id}'

        db.executar_query(query, dados)

    @classmethod
    def excluir(cls, condicao):
        query = f'DELETE FROM consultas WHERE {condicao}'
        db.executar_query(query)


if __name__ == '__main__':
    dados = [
        ('08604635165', '33965093584', '05/04/2024', '15:00'),
        ('24462222695', '37522138418', '05/04/2024', '15:00'),
        ('25370642320', '37999371882', '05/04/2024', '15:00'),
        ('30884638707', '50952169304', '05/04/2024', '15:00'),
    ]

    for i in dados:
        Consulta.adicionar(*i)

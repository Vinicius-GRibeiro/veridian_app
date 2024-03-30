from _conexao import Conexao
db = Conexao()


class Endereco:
    @classmethod
    def adicionar(cls, cep: str, rua: str, numero: str, bairro: str, cidade: str, estado: str, complemento: str = None):
        query = '''
            INSERT INTO enderecos (cep, rua, numero, bairro, cidade, estado, complemento) values (?, ?, ?, ?, ?, ?, ?)
        '''
        dados = (cep, rua, numero, bairro, cidade, estado, complemento,)

        db.executar_query(query, dados)

    @classmethod
    def buscar(cls, colunas='*', condicao=None):
        query = f'SELECT {colunas} from enderecos'

        if condicao is not None:
            query += f' WHERE {condicao}'

        dados = db.executar_query(query, operacao_de_consulta=True)
        print(dados)

    @classmethod
    def editar(cls, id: int, dicionario_campo_valor):
        campos = ', '.join([f"{campo} = ?" for campo in dicionario_campo_valor.keys()])

        dados = tuple(dicionario_campo_valor.values())
        query = f'UPDATE enderecos SET {campos} WHERE id = {id}'

        db.executar_query(query, dados)

    @classmethod
    def excluir(cls, condicao):
        query = f'DELETE FROM enderecos WHERE {condicao}'
        db.executar_query(query)


# ceps = ['12922-290', '01001-000', '05379-150', '57303-785', '40255-175', '69313-292', '41339-612', '89803-098',
#         '50940-043', '54270-800', '25240-570', '41311-212', '78053-678', '78115-030', '69077-130', '44573-580']
#
# for c in ceps:
#     resposta = requests.get(f'http://www.viacep.com.br/ws/{c.replace('-', '')}/json/')
#     dados = resposta.json()
#
#     cep = dados['cep'].replace('-', '')
#     EnderecoController.adicionar(cep=cep, rua=dados['logradouro'], numero=dados['gia'], bairro=dados['bairro'],
#                                  cidade=dados['localidade'], estado=dados['uf'], complemento=dados['complemento'])

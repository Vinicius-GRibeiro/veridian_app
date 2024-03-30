from _conexao import Conexao

db = Conexao()


class Contato:
    @classmethod
    def adicionar(self, cel1: str, cel2: str, email: str):
        query = '''
            INSERT INTO contatos (cel1, cel2, email) values (?, ?, ?)
        '''
        dados = (cel1, cel2, email)

        db.executar_query(query, dados)

    @classmethod
    def buscar(self, colunas='*', condicao=None):
        query = f'SELECT {colunas} from contatos'

        if condicao is not None:
            query += f' WHERE {condicao}'

        dados = db.executar_query(query, operacao_de_consulta=True)
        return dados

    @classmethod
    def editar(self, id: int, dicionario_campo_valor):
        campos = ', '.join([f"{campo} = ?" for campo in dicionario_campo_valor.keys()])

        dados = tuple(dicionario_campo_valor.values())
        query = f'UPDATE contatos SET {campos} WHERE id = {id}'

        db.executar_query(query, dados)

    @classmethod
    def excluir(self, condicao):
        query = f'DELETE FROM contatos WHERE {condicao}'
        db.executar_query(query)


# cel1 = ['(68) 3346-6364', '(97) 2861-2128', '(82) 2373-3213', '(95) 3426-5064', '(64) 3314-8355', '(62) 3564-4137',
#         '(69) 2592-8850', '(51) 2172-3815', '(95) 3317-9825', '(28) 2459-7506', '(86) 3031-4251', '(69) 3218-2652']
#
# cel2 = ['(85) 2231-4013', '(92) 2498-6112', '(41) 2484-8188', '(49) 2723-8431', '(94) 2967-4645', '(28) 2154-3562',
#         '(84) 3623-8395', '(81) 3721-6525', '(82) 2745-4105', '(91) 3433-1274', '(13) 3495-2802', '(19) 3554-8493']
#
# email = [
#     'yurioliveira_pereira87@gmail.com', 'yurioliveira_pereira87@gmail.com', 'margaridaoliveira.reis17@live.com',
#     'fabrciamelo.moraes61@gmail.com', 'silassilva22@yahoo.com', 'nbiasantos.reis15@hotmail.com',
#     'csarcarvalho71@yahoo.com', 'fabrciaxavier_costa21@yahoo.com', 'lviasaraiva70@live.com',
#     'eduardaxavier.braga@hotmail.com', 'carloscosta.batista91@yahoo.com', 'alicexavier94@hotmail.com'
# ]
#
# for i in range(12):
#     Contato.adicionar(cel1[i], cel2[i], email[i])

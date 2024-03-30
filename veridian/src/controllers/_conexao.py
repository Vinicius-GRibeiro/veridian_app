import sqlite3
import logging


class GerenciadorDeLogs:
    def __init__(self):
        self.nome_arquivo = 'veridian.log'
        self.formato = '%(asctime)s - %(levelname)s - %(message)s'
        self.formato_data = '%d/%m/%Y - %H:%M'
        self.logger = logging.getLogger('GerenciadorDeLogs')

        logging.basicConfig(filename=self.nome_arquivo, format=self.formato, datefmt=self.formato_data,
                            level=logging.ERROR, encoding='utf-8')

    def erro(self, mensagem, e, query=None):
        mensagem = f'{mensagem}\n\tErro: {e}'

        if query is not None:
            mensagem += f'\n\tQuery: {query}'

        self.logger.error(msg=mensagem)


log = GerenciadorDeLogs()
erros = (BaseException, sqlite3.Error)


class Conexao:
    def __init__(self):
        self.conexao = None
        self.cursor = None

    def abrir_conexao(self):
        try:
            self.conexao = sqlite3.connect('veridian.db')
            self.cursor = self.conexao.cursor()
        except erros as e:
            log.erro(mensagem='Houve um erro ao abrir a conexão com o banco', e=e)

    def fechar_conexao(self):
        try:
            self.cursor.close()
            self.conexao.close()
        except erros as e:
            log.erro(mensagem='Houve um erro ao encerrar a conexão com o banco', e=e)

    def executar_query(self, query, dados=None, operacao_de_consulta=False):
        try:
            self.abrir_conexao()

            retorno = self.cursor.execute(query, dados) if dados is not None else self.cursor.execute(query)

            if operacao_de_consulta:
                retorno = self.cursor.fetchall()

            self.conexao.commit()
            self.fechar_conexao()
            return retorno
        except erros as e:
            log.erro(mensagem='Houve um erro inserir dados', e=e, query=query)
            return None

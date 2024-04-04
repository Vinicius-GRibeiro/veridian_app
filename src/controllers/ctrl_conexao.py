import sqlite3
import logging
import os
from pprint import pprint


class GerenciadorDeLogs:
    def __init__(self):
        self.nome_arquivo = "C:\\Users\\vi_mt\\OneDrive\\Área de Trabalho\\veridian.log"
        self.formato = '%(asctime)s - %(levelname)s - %(message)s'
        self.formato_data = '%d/%m/%Y - %H:%M'
        self.logger = logging.getLogger('GerenciadorDeLogs')
        self.logger.setLevel(logging.ERROR)  # Definir o nível do logger

        # Criar um manipulador de arquivo
        file_handler = logging.FileHandler(self.nome_arquivo, mode='a', encoding='utf-8')
        file_handler.setLevel(logging.ERROR)  # Definir o nível do manipulador de arquivo

        # Definir o formato do log
        formatter = logging.Formatter(self.formato, datefmt=self.formato_data)
        file_handler.setFormatter(formatter)

        # Adicionar o manipulador ao logger
        self.logger.addHandler(file_handler)

    def erro(self, mensagem, e, query=None):
        mensagem = f'{mensagem}\n\tErro: {e}'

        if query is not None:
            mensagem += f'\n\tQuery: {query}'

        self.logger.exception(mensagem)


log = GerenciadorDeLogs()


class Conexao:
    def __init__(self):
        self.conexao = None
        self.cursor = None

    def abrir_conexao(self):
        try:
            self.conexao = sqlite3.connect("C:\\Users\\vi_mt\\OneDrive\\Área de Trabalho\\veridian.db")
            self.cursor = self.conexao.cursor()
        except sqlite3.Error as e:
            log.erro(mensagem='Houve um erro ao abrir a conexão com o banco', e=e)

    def fechar_conexao(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conexao:
                self.conexao.close()
        except sqlite3.Error as e:
            log.erro(mensagem='Houve um erro ao encerrar a conexão com o banco', e=e)

    def executar_query(self, query, dados=None, operacao_de_consulta=False):
        try:
            self.abrir_conexao()

            if dados is not None:
                self.cursor.execute(query, dados)
            else:
                self.cursor.execute(query)

            if operacao_de_consulta:
                retorno = self.cursor.fetchall()
            else:
                retorno = None

            self.conexao.commit()
            return retorno
        except sqlite3.Error as e:
            log.erro(mensagem='Houve um erro ao executar a query', e=e, query=query)
            return None
        finally:
            self.fechar_conexao()

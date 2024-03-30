import sqlite3
from _conexao import Conexao

db = Conexao()


def criar_tabelas():
    query_criar_tabela_enderecos = '''
        CREATE TABLE IF NOT EXISTS enderecos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cep TEXT,
            rua TEXT,
            numero TEXT,
            bairro TEXT,
            cidade TEXT, 
            estado TEXT,
            complemento TEXT
        )
    '''

    query_criar_tabela_contatos = '''
        CREATE TABLE IF NOT EXISTS contatos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cel1 TEXT,
            cel2 TEXT,
            email TEXT
        )
    '''

    query_criar_tabela_usuarios = '''
        CREATE TABLE IF NOT EXISTS usuarios(
            cpf TEXT PRIMARY KEY,
            nome TEXT,
            rg TEXT,
            nascimento TEXT,
            genero TEXT,
            id_endereco INTEGER,
            id_contato INTEGER,
            FOREIGN KEY (id_endereco) REFERENCES enderecos(id),
            FOREIGN KEY (id_contato) REFERENCES contatos(id)
        )
    '''

    query_criar_tabela_pacientes = '''
        CREATE TABLE IF NOT EXISTS pacientes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rh TEXT,
            alergias TEXT,
            convenio TEXT,
            cpf_usuario TEXT,
            FOREIGN KEY (cpf_usuario) REFERENCES usuarios   (cpf)
        )
    '''

    query_criar_tabela_medicos = '''
            CREATE TABLE IF NOT EXISTS medicos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                crm TEXT,
                especialidade TEXT,
                cpf_usuario TEXT,
                FOREIGN KEY (cpf_usuario) REFERENCES usuarios(cpf)
            )
        '''

    query_criar_tabela_funcionarios = '''
                CREATE TABLE IF NOT EXISTS funcionarios(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cargo TEXT,
                    cpf_usuario TEXT,
                    FOREIGN KEY (cpf_usuario) REFERENCES usuarios(cpf)
                )
            '''

    query_criar_tabela_credenciais = '''
        CREATE TABLE IF NOT EXISTS credenciais(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT,
            senha TEXT,
            cpf_usuario TEXT,
            FOREIGN KEY (cpf_usuario) REFERENCES usuarios(cpf)
        )
    '''

    queries = [
        query_criar_tabela_enderecos,
        query_criar_tabela_contatos,
        query_criar_tabela_usuarios,
        query_criar_tabela_pacientes,
        query_criar_tabela_medicos,
        query_criar_tabela_funcionarios,
        query_criar_tabela_credenciais
    ]

    db.abrir_conexao()

    for query in queries:
        db.cursor.execute(query)
    db.conexao.commit()
    db.fechar_conexao()


criar_tabelas()

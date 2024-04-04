from src.controllers.ctrl_conexao import Conexao


db = Conexao()


class Usuario:
    @classmethod
    def adicionar(cls, cpf: str, nome: str, rg: str, nascimento: int, genero: str, id_endereco: int, id_contato: int, img: str):
        query = '''
            INSERT INTO usuarios (cpf, nome, rg, nascimento, genero, id_endereco, id_contato, img)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        dados = (cpf, nome, rg, nascimento, genero, id_endereco, id_contato, img)

        db.executar_query(query, dados)

    @classmethod
    def buscar(cls, colunas='*', condicao=None):
        query = f'SELECT {colunas} from usuarios'

        if condicao is not None:
            query += f' WHERE {condicao}'
        dados = db.executar_query(query, operacao_de_consulta=True)
        dados_ = None

        if dados is not None:
            dados_ = [x[0] for x in dados]

        return dados_

    @classmethod
    def editar(cls, id: int, dicionario_campo_valor):
        campos = ', '.join([f"{campo} = ?" for campo in dicionario_campo_valor.keys()])

        dados = tuple(dicionario_campo_valor.values())
        query = f'UPDATE usuarios SET {campos} WHERE id = {id}'

        db.executar_query(query, dados)

    @classmethod
    def excluir(cls, condicao):
        query = f'DELETE FROM usuarios WHERE {condicao}'
        db.executar_query(query)


if __name__ == '__main__':
    dados = [
        {
            "nome": "Marina Agatha da Cunha",
            "idade": 24,
            "cpf": "08604635165",
            "rg": "447430397",
            "data_nasc": "06/02/2000",
            "sexo": "Feminino",
            "signo": "Aquário",
            "mae": "Simone Rita Bianca",
            "pai": "Vitor Cauã da Cunha",
            "email": "marina.agatha.dacunha@negocios-de-valor.com",
            "senha": "e5wLX4tusA",
            "cep": "78065408",
            "endereco": "Rua Espanha",
            "numero": 663,
            "bairro": "Jardim Europa",
            "cidade": "Cuiabá",
            "estado": "MT",
            "telefone_fixo": "6525326716",
            "celular": "65988393860",
            "altura": "1,61",
            "peso": 49,
            "tipo_sanguineo": "A-",
            "cor": "vermelho"
        },
        {
            "nome": "Bruno Giovanni Castro",
            "idade": 73,
            "cpf": "88700210170",
            "rg": "405421205",
            "data_nasc": "20/02/1951",
            "sexo": "Masculino",
            "signo": "Peixes",
            "mae": "Rosângela Helena Hadassa",
            "pai": "Iago Manoel Vinicius Castro",
            "email": "brunogiovannicastro@iq.unesp.br",
            "senha": "yMjOoTpNyZ",
            "cep": "57015232",
            "endereco": "2ª Travessa Bom Retiro",
            "numero": 673,
            "bairro": "Vergel do Lago",
            "cidade": "Maceió",
            "estado": "AL",
            "telefone_fixo": "8237254274",
            "celular": "82992139714",
            "altura": "1,61",
            "peso": 88,
            "tipo_sanguineo": "B+",
            "cor": "roxo"
        },
        {
            "nome": "Larissa Isabelly Analu Assis",
            "idade": 36,
            "cpf": "24462222695",
            "rg": "141538302",
            "data_nasc": "21/01/1988",
            "sexo": "Feminino",
            "signo": "Aquário",
            "mae": "Isabella Liz Regina",
            "pai": "Leandro Isaac Assis",
            "email": "larissa_isabelly_assis@esplanadaviagens.com.br",
            "senha": "STBBb1LmIL",
            "cep": "69915028",
            "endereco": "Rua Longuinho da Silva",
            "numero": 916,
            "bairro": "Conjunto Tangará",
            "cidade": "Rio Branco",
            "estado": "AC",
            "telefone_fixo": "6826776275",
            "celular": "68982027000",
            "altura": "1,61",
            "peso": 51,
            "tipo_sanguineo": "A-",
            "cor": "verde"
        },
        {
            "nome": "Kauê Cláudio Moreira",
            "idade": 68,
            "cpf": "37999371882",
            "rg": "108496181",
            "data_nasc": "17/03/1956",
            "sexo": "Masculino",
            "signo": "Peixes",
            "mae": "Andreia Yasmin",
            "pai": "Otávio André Enzo Moreira",
            "email": "kaue_moreira@cernizza.com.br",
            "senha": "DsIfi2uzD1",
            "cep": "64050010",
            "endereco": "Avenida Homero Castelo Branco",
            "numero": 772,
            "bairro": "Planalto",
            "cidade": "Teresina",
            "estado": "PI",
            "telefone_fixo": "8635634199",
            "celular": "86981835604",
            "altura": "1,64",
            "peso": 97,
            "tipo_sanguineo": "A+",
            "cor": "laranja"
        },
        {
            "nome": "Bento Ruan Kauê Alves",
            "idade": 60,
            "cpf": "37522138418",
            "rg": "488863107",
            "data_nasc": "26/02/1964",
            "sexo": "Masculino",
            "signo": "Peixes",
            "mae": "Tânia Marli",
            "pai": "Leonardo Pietro Juan Alves",
            "email": "bento.ruan.alves@owl-ti.com.br",
            "senha": "Yx1asxFRBi",
            "cep": "84032469",
            "endereco": "Rua Manoel Sansana",
            "numero": 911,
            "bairro": "Cará-cará",
            "cidade": "Ponta Grossa",
            "estado": "PR",
            "telefone_fixo": "4239188270",
            "celular": "42985157338",
            "altura": "2,00",
            "peso": 89,
            "tipo_sanguineo": "B+",
            "cor": "amarelo"
        },
        {
            "nome": "Bryan Paulo Rocha",
            "idade": 72,
            "cpf": "30884638707",
            "rg": "351681620",
            "data_nasc": "04/01/1952",
            "sexo": "Masculino",
            "signo": "Capricórnio",
            "mae": "Manuela Rafaela Stefany",
            "pai": "Filipe Davi Benício Rocha",
            "email": "bryan_paulo_rocha@bplan.com.br",
            "senha": "NDDp72jeT2",
            "cep": "68960971",
            "endereco": "Vila Carnot, s/n",
            "numero": 329,
            "bairro": "Vila Carnot",
            "cidade": "Calçoene",
            "estado": "AP",
            "telefone_fixo": "9635295037",
            "celular": "96989354149",
            "altura": "1,68",
            "peso": 102,
            "tipo_sanguineo": "AB-",
            "cor": "azul"
        },
        {
            "nome": "Raquel Natália Raquel Santos",
            "idade": 45,
            "cpf": "50952169304",
            "rg": "361129579",
            "data_nasc": "13/03/1979",
            "sexo": "Feminino",
            "signo": "Peixes",
            "mae": "Hadassa Nina",
            "pai": "Caio Mário Gael Santos",
            "email": "raquelnataliasantos@budsoncorporation.com",
            "senha": "srB9QFMPjf",
            "cep": "79645506",
            "endereco": "Rua José Amim",
            "numero": 558,
            "bairro": "Jardim Oiti",
            "cidade": "Três Lagoas",
            "estado": "MS",
            "telefone_fixo": "6729328682",
            "celular": "67981740806",
            "altura": "1,65",
            "peso": 51,
            "tipo_sanguineo": "AB-",
            "cor": "roxo"
        },
        {
            "nome": "Bento Vitor Nascimento",
            "idade": 28,
            "cpf": "33965093584",
            "rg": "373382698",
            "data_nasc": "13/01/1996",
            "sexo": "Masculino",
            "signo": "Capricórnio",
            "mae": "Joana Eliane",
            "pai": "Otávio Murilo Nascimento",
            "email": "bento.vitor.nascimento@yahoo.com",
            "senha": "FAbG2aQTrO",
            "cep": "49020470",
            "endereco": "Rua Américo Curvelo",
            "numero": 473,
            "bairro": "Salgado Filho",
            "cidade": "Aracaju",
            "estado": "SE",
            "telefone_fixo": "7928543530",
            "celular": "79995384535",
            "altura": "1,84",
            "peso": 53,
            "tipo_sanguineo": "AB-",
            "cor": "laranja"
        },
        {
            "nome": "Felipe Arthur Julio Baptista",
            "idade": 25,
            "cpf": "94648913353",
            "rg": "356780211",
            "data_nasc": "06/03/1999",
            "sexo": "Masculino",
            "signo": "Peixes",
            "mae": "Rita Caroline",
            "pai": "Daniel Giovanni Baptista",
            "email": "felipe_baptista@stilomovelaria.com.br",
            "senha": "ulaMsszihG",
            "cep": "99711272",
            "endereco": "Rua José Ferrazzo",
            "numero": 644,
            "bairro": "Koller",
            "cidade": "Erechim",
            "estado": "RS",
            "telefone_fixo": "5439146078",
            "celular": "54992075396",
            "altura": "1,74",
            "peso": 59,
            "tipo_sanguineo": "A-",
            "cor": "azul"
        },
        {
            "nome": "Elaine Raimunda Vera Araújo",
            "idade": 42,
            "cpf": "25370642320",
            "rg": "242650375",
            "data_nasc": "13/03/1982",
            "sexo": "Feminino",
            "signo": "Peixes",
            "mae": "Maya Nina Emilly",
            "pai": "Leandro Gael Araújo",
            "email": "elaineraimundaaraujo@victorseguros.com.br",
            "senha": "YddUEnMlZT",
            "cep": "75905800",
            "endereco": "Avenida Demolíncio de Carvalho",
            "numero": 575,
            "bairro": "Parque Bandeirante",
            "cidade": "Rio Verde",
            "estado": "GO",
            "telefone_fixo": "6435372944",
            "celular": "64994905785",
            "altura": "1,67",
            "peso": 54,
            "tipo_sanguineo": "B+",
            "cor": "azul"
        },
        {
            "nome": "Mário Miguel Heitor Costa",
            "idade": 45,
            "cpf": "87960970602",
            "rg": "239936723",
            "data_nasc": "25/01/1979",
            "sexo": "Masculino",
            "signo": "Aquário",
            "mae": "Lorena Fabiana Joana",
            "pai": "Kevin Enrico Matheus Costa",
            "email": "mario.miguel.costa@mosman.com.br",
            "senha": "etbtFKctE2",
            "cep": "77015422",
            "endereco": "Quadra 305 Sul Avenida NS 5",
            "numero": 797,
            "bairro": "Plano Diretor Sul",
            "cidade": "Palmas",
            "estado": "TO",
            "telefone_fixo": "6335068831",
            "celular": "63999851707",
            "altura": "1,98",
            "peso": 79,
            "tipo_sanguineo": "AB+",
            "cor": "amarelo"
        },
        {
            "nome": "Pedro Gabriel Caldeira",
            "idade": 21,
            "cpf": "53406890857",
            "rg": "394792567",
            "data_nasc": "09/02/2003",
            "sexo": "Masculino",
            "signo": "Aquário",
            "mae": "Isabel Tereza Manuela",
            "pai": "Cauê Carlos Eduardo Otávio Caldeira",
            "email": "pedrogabrielcaldeira@alwan.com.br",
            "senha": "xE92B1oA71",
            "cep": "76964042",
            "endereco": "Avenida Carlos Gomes",
            "numero": 878,
            "bairro": "Princesa Isabel",
            "cidade": "Cacoal",
            "estado": "RO",
            "telefone_fixo": "6927139752",
            "celular": "69986778129",
            "altura": "1,76",
            "peso": 65,
            "tipo_sanguineo": "A+",
            "cor": "roxo"
        }
    ]

    for n, u in enumerate(dados):
        Usuario.adicionar(
            cpf=u['cpf'], nome=u['nome'], rg=u['rg'], genero=u['sexo'],
            nascimento=u['data_nasc'], id_contato=n+20, id_endereco=n+20
        )


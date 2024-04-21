import flet as ft
from src.controllers.ctrl_medico import Medico
from src.controllers.ctrl_usuarios import Usuario
from src.controllers.ctrl_consultas import Consulta
from src.models.vw_models.mdl_vw_historico_consultas import ContainerConsulta
from src.controllers.ctrl_data_horario import formatar_dd_mm_aaaa, gerar_timestamp

ID_CONTROLE_DATA_INICIAL = '_69'
ID_CONTROLE_DATA_FINAL = '_72'


class CalendarioFiltroDeConsulta:
    def __init__(self, pagina: ft.Page,
                 is_inicial: bool = None):
        self.pagina = pagina
        self.is_inicial = is_inicial
        self.get = self._get()

    def _ao_selecionar_data(self, e: ft.ControlEvent):
        if self.pagina.session.get('data_final_inicial') == 'inicial':
            self.pagina.get_control(ID_CONTROLE_DATA_INICIAL).value = formatar_dd_mm_aaaa(str(e.control.value))
        elif self.pagina.session.get('data_final_inicial') == 'final':
            self.pagina.get_control(ID_CONTROLE_DATA_FINAL).value = formatar_dd_mm_aaaa(str(e.control.value))
        self.pagina.update()

    def _get(self) -> ft.DatePicker:
        dp = ft.DatePicker(
            cancel_text='cancelar',
            confirm_text='ok',
            date_picker_entry_mode=ft.DatePickerEntryMode.CALENDAR_ONLY,
            help_text='Selecione uma data',
            on_change=lambda e: self._ao_selecionar_data(e)
        )

        return dp


class CaixaDeEscolhaEspecialidades:
    def __init__(self, pagina: ft.Page):
        self.pagina = pagina
        self.opcoes = []
        self.get = self._get()

    def _get(self) -> ft.Dropdown:
        dp = ft.Dropdown(
            border_radius=10,
            expand=True,
            hint_text='selecione uma especialidade',
            filled=True,
            bgcolor='white',
            height=60,
            border_color='#004D40',
            border_width=1
        )

        return dp

    def atualizar_opcoes(self):
        opcoes = [item[0] for item in Medico.buscar_unicos(colunas='especialidade')]

        self.get.options.clear()
        for especialidade in opcoes:
            self.get.options.append(
                ft.dropdown.Option(especialidade.capitalize())
            )


class ChipStatusConsulta:
    def __init__(self, pagina: ft.Page, label: str, icone: str, cor_icone: str):
        self.pagina = pagina
        self.label = label
        self.icone = icone
        self.cor_icone = cor_icone
        self.get = self._get()

    @staticmethod
    def mudar_cor_ao_ser_selecionado(controle: ft.Chip):
        if controle.selected:
            controle.label_style = ft.TextStyle(
                color='#FFFFFF',
                font_family='nunito-regular'
            )

    def _get(self) -> ft.Chip:
        c = ft.Chip(
            label=ft.Text(value=self.label, color='#222222', font_family='nunito-regular'),
            label_style=ft.TextStyle(
                color='#2222222',
                font_family='nunito-regular'
            ),
            leading=ft.Icon(name=self.icone, color=self.cor_icone),
            selected_color='0BAB7D',
            show_checkmark=False,
            on_select=lambda e: ...
        )

        return c


class CardFiltrosDeConsultas:
    def __init__(self, pagina: ft.Page, funcao_refresh):
        self.pagina = pagina
        self._padding_padrao = 15

        self.chip_filtro_agendado = ChipStatusConsulta(label='Agendado', icone=ft.icons.DATE_RANGE_ROUNDED,
                                                       pagina=self.pagina, cor_icone='#FF9F1C')
        self.chip_filtro_realizado = ChipStatusConsulta(label='Realizado', icone=ft.icons.DONE_ALL_ROUNDED,
                                                        pagina=self.pagina, cor_icone='#0BAB7D')
        self.chip_filtro_cancelado = ChipStatusConsulta(label='Cancelado', icone=ft.icons.CANCEL_ROUNDED,
                                                        pagina=self.pagina, cor_icone='#DE1A1A')
        self.caixa_de_escolha_especialidades = CaixaDeEscolhaEspecialidades(self.pagina)
        self.caixa_de_escolha_especialidades.atualizar_opcoes()

        self.texto_data_inicial = ft.Text(value='data inicial', font_family='nunito-regular', color='#222222')

        self.texto_data_final = ft.Text(value='data final', font_family='nunito-regular', color='#222222')

        self.query_geral = None

        self.funcao_refresh = funcao_refresh

        self.get = self._get()

    def ao_fechar_filtros(self):
        self.chip_filtro_agendado.get.selected = False
        self.chip_filtro_cancelado.get.selected = False
        self.chip_filtro_realizado.get.selected = False
        self.caixa_de_escolha_especialidades.atualizar_opcoes()
        self.caixa_de_escolha_especialidades.get.value = None
        self.texto_data_inicial.value = 'data inicial'
        self.texto_data_final.value = 'data final'
        self.pagina.update()

    def _ao_clicar_escolher_data(self, is_inicial: bool):
        self.pagina.session.set('data_final_inicial', 'inicial' if is_inicial else 'final')
        self.pagina.overlay[0].pick_date()

    def _get(self) -> ft.Column:
        bs = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        ft.Container(
                            padding=ft.padding.only(right=25),
                            content=ft.IconButton(icon=ft.icons.REFRESH_ROUNDED, on_click=self.funcao_refresh)
                        )
                    ]
                ),

                ft.Container(height=10),

                ft.Container(
                    padding=ft.padding.only(right=self._padding_padrao, left=self._padding_padrao),
                    content=ft.Row(
                        spacing=10,
                        controls=[
                            ft.Icon(name=ft.icons.NEW_RELEASES_ROUNDED, color='#222222', size=20),
                            ft.Text(value='Status da consulta', font_family='nunito-regular', color='#222222')
                        ]
                    )
                ),

                ft.Container(height=10),

                ft.Container(
                    padding=ft.padding.only(right=self._padding_padrao, left=self._padding_padrao),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            self.chip_filtro_realizado.get,
                            self.chip_filtro_agendado.get,
                            self.chip_filtro_cancelado.get,
                        ]
                    )
                ),

                ft.Container(height=25),

                ft.Container(
                    padding=ft.padding.only(right=self._padding_padrao, left=self._padding_padrao),
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            ft.Icon(name=ft.icons.HEALTH_AND_SAFETY_ROUNDED, color='#222222', size=20),
                            ft.Text(value='Especialidade médica', font_family='nunito-regular', color='#222222')
                        ]
                    )
                ),

                ft.Container(height=10),

                ft.Container(
                    padding=ft.padding.only(right=self._padding_padrao, left=self._padding_padrao),
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            self.caixa_de_escolha_especialidades.get
                        ]
                    )
                ),

                ft.Container(height=25),

                ft.Container(
                    padding=ft.padding.only(right=self._padding_padrao, left=self._padding_padrao),
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            ft.Icon(name=ft.icons.HEALTH_AND_SAFETY_ROUNDED, color='#222222', size=20),
                            ft.Text(value='Data da consulta', font_family='nunito-regular', color='#222222')
                        ]
                    )
                ),

                ft.Container(height=10),

                ft.Container(
                    padding=ft.padding.only(right=self._padding_padrao, left=self._padding_padrao + 10),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        spacing=10,
                        controls=[
                            ft.Text(value='de', font_family='nunito-bold'),

                            ft.Container(
                                padding=ft.padding.only(right=self._padding_padrao, left=self._padding_padrao),
                                border_radius=12, width=150, height=40, alignment=ft.alignment.center,
                                border=ft.Border(ft.BorderSide(1, '#222222'), ft.BorderSide(1, '#222222'),
                                                 ft.BorderSide(1, '#222222'), ft.BorderSide(1, '#222222')),
                                content=self.texto_data_inicial,
                                bgcolor='white',
                                on_click=lambda e: self._ao_clicar_escolher_data(True)
                            ),

                            ft.Text(value='até', font_family='nunito-bold'),

                            ft.Container(
                                padding=ft.padding.only(right=self._padding_padrao, left=self._padding_padrao),
                                border_radius=12, width=150, height=40, alignment=ft.alignment.center,
                                border=ft.Border(ft.BorderSide(1, '#222222'), ft.BorderSide(1, '#222222'),
                                                 ft.BorderSide(1, '#222222'), ft.BorderSide(1, '#222222')),
                                content=self.texto_data_final,
                                bgcolor='white',
                                on_click=lambda e: self._ao_clicar_escolher_data(False)
                            ),
                        ]
                    )
                ),

                ft.Container(height=20),

            ]
        )

        return bs


class HistoricoConsultas:
    def __init__(self, page: ft.Page):
        self.pagina = page
        self.user_cpf = self.pagina.session.get('user_cpf')

        self.lista_de_cards_de_consulta = []

        self.filtros_de_consulta = CardFiltrosDeConsultas(self.pagina, lambda e: self._resetar_filtros())

        self.filtros_de_consulta_holder = ft.ExpansionTile(
            leading=ft.Icon(name=ft.icons.FILTER_ALT, color='#222222'),
            title=ft.Text("Filtrar consultas", font_family='nunito-bold', color='#222222'),
            trailing=ft.IconButton(icon=ft.icons.DONE_ROUNDED, icon_color='#222222',
                                   on_click=lambda e: self._ao_clicar_aplicar_filtros()),

            bgcolor='#C5E1A5',
            collapsed_bgcolor='#0BAB7D',
            controls=[
                self.filtros_de_consulta.get
            ],
            on_change=lambda e: self.filtros_de_consulta.ao_fechar_filtros(),
        )

        self.dados_para_o_cartao = []
        self._get_dados_consultas()

        for item in self.dados_para_o_cartao:
            self.lista_de_cards_de_consulta.append(
                ContainerConsulta(*item).get
            )

        self.get_view = self._get_view()

    def _get_dados_consultas(self):
        query = self.filtros_de_consulta.query_geral if self.filtros_de_consulta.query_geral is not None else None
        dados_consulta = Consulta.buscar(condicao=query) if query else Consulta.buscar(
            condicao=f"cpf_paciente = '{self.user_cpf}'",
            ordenar_por='timestamp'
        )

        self.dados_para_o_cartao.clear()

        for item in dados_consulta:
            id_consulta, cpf_medico, status, timestamp, especialidade, obs = item[0], item[2], item[3], item[4], item[
                5], item[6]
            crm = Medico.buscar_unicos(colunas='crm', condicao=f"cpf_usuario = '{cpf_medico}'")[0][0]

            dados_medico = Usuario.buscar(colunas='nome, genero, img', condicao=f"cpf = '{cpf_medico}'")

            nome_medico = dados_medico[0][0]
            genero_medico = dados_medico[0][1]
            imagem_medico = dados_medico[0][2]

            self.dados_para_o_cartao.append(
                (id_consulta, status, timestamp, especialidade, obs, crm, nome_medico, genero_medico, imagem_medico)
            )

    def _atualizar_coluna_de_cards(self):
        self.lista_de_cards_de_consulta.clear()
        for item in self.dados_para_o_cartao:
            self.lista_de_cards_de_consulta.append(
                ContainerConsulta(*item).get
            )

        self.pagina.update()

    def _ao_clicar_aplicar_filtros(self):
        query_geral = ''
        controlador_de_procedencia = False

        if self.filtros_de_consulta.chip_filtro_realizado.get.selected:
            query_geral += f" OR status = 'realizado'" if len(query_geral) > 0 else f" status = 'realizado'"
            controlador_de_procedencia = True

        if self.filtros_de_consulta.chip_filtro_agendado.get.selected:
            query_geral += f" OR status = 'agendado'" if len(query_geral) > 0 else f" status = 'agendado'"
            controlador_de_procedencia = True

        if self.filtros_de_consulta.chip_filtro_cancelado.get.selected:
            query_geral += f" OR status = 'cancelado'" if len(query_geral) > 0 else f" status = 'cancelado'"
            controlador_de_procedencia = True

        if controlador_de_procedencia:
            query_geral = f"({query_geral})"

        if self.filtros_de_consulta.caixa_de_escolha_especialidades.get.value is not None:
            query_geral += f" AND especialidade = '{self.filtros_de_consulta.caixa_de_escolha_especialidades.get.value.lower()}'" \
                if len(
                query_geral) > 0 else f" especialidade = '{self.filtros_de_consulta.caixa_de_escolha_especialidades.get.value.lower()}'"

        if self.filtros_de_consulta.texto_data_inicial.value != 'data inicial':
            query_geral += f" AND timestamp >= {gerar_timestamp(data=self.filtros_de_consulta.texto_data_inicial.value)}" \
                if len(
                query_geral) > 0 else f" timestamp >= {gerar_timestamp(data=self.filtros_de_consulta.texto_data_inicial.value)}"

        if self.filtros_de_consulta.texto_data_final.value != 'data final':
            query_geral += f" AND timestamp <= {gerar_timestamp(data=self.filtros_de_consulta.texto_data_final.value)}" \
                if len(
                query_geral) > 0 else f" timestamp <= {gerar_timestamp(data=self.filtros_de_consulta.texto_data_final.value)}"

        if len(query_geral) > 0:
            query_geral += f" AND cpf_paciente = '{self.filtros_de_consulta.pagina.session.get('user_cpf')}'"

        self.filtros_de_consulta.query_geral = query_geral

        self._get_dados_consultas()
        self._atualizar_coluna_de_cards()

    def _resetar_filtros(self):
        self.filtros_de_consulta.query_geral = f"cpf_paciente = '{self.user_cpf}'"

        self._get_dados_consultas()
        self._atualizar_coluna_de_cards()

    def _get_view(self) -> ft.Column:
        view = ft.Column(
            spacing=0,
            controls=[
                ft.Column(
                    spacing=0,
                    controls=[
                        self.filtros_de_consulta_holder,
                        ft.Container(height=20),
                    ]
                ),

                ft.Column(
                    spacing=10,
                    controls=self.lista_de_cards_de_consulta
                )
            ]
        )
        return view

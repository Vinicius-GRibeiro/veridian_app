import flet as ft
from src.controllers.ctrl_medico import Medico
from src.controllers.ctrl_data_horario import formatar_dd_mm_aaaa

ID_CONTROLE_DATA_INICIAL = '_77'
ID_CONTROLE_DATA_FINAL = '_80'


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
            label='selecione uma especialidade'
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

    def _ao_clicar(self, e: ft.ControlEvent):
        if self.label == 'Agendado' and e.control.selected:
            print('agendado')
        elif self.label == 'Cancelado' and e.control.selected:
            print('cancelado')
        elif self.label == 'Realizado' and e.control.selected:
            print('realizado')

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
            on_select=lambda e: self._ao_clicar(e)
        )

        return c


class CardFiltrosDeConsultas:
    def __init__(self, pagina: ft.Page):
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

        self.get = self._get()

    def _ao_ignorar_caixa(self):
        self.chip_filtro_agendado.get.selected = False
        self.chip_filtro_cancelado.get.selected = False
        self.chip_filtro_realizado.get.selected = False
        self.caixa_de_escolha_especialidades.atualizar_opcoes()
        self.caixa_de_escolha_especialidades.get.value = ''
        self.texto_data_inicial.value = ''
        self.texto_data_final.value = ''

    def _ao_clicar_escolher_data(self, e: ft.ControlEvent, is_inicial: bool):
        self.pagina.session.set('data_final_inicial', 'inicial' if is_inicial else 'final')
        self.pagina.overlay[1].pick_date()

    def _get(self) -> ft.BottomSheet:
        bs = ft.BottomSheet(
            enable_drag=True,
            on_dismiss=lambda e: self._ao_ignorar_caixa(),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                controls=[
                    ft.Container(
                        padding=ft.padding.only(top=10),
                        content=ft.Container(
                            height=3,
                            width=70,
                            border_radius=16,
                            bgcolor='#646F67'
                        )
                    ),

                    ft.Container(
                        padding=ft.padding.only(left=self._padding_padrao, right=self._padding_padrao, top=10),
                        content=ft.Row(
                            spacing=0,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Text('Filtros de consulta', font_family='nunito-bold', color='#222222'),
                                ft.TextButton(content=ft.Row(
                                    controls=[
                                        ft.Text(value='Aplicar filtros', color='#0BAB7D',
                                                font_family='nunito-regular'),
                                        ft.Icon(name=ft.icons.DONE_ROUNDED, color='#0BAB7D'),
                                    ]
                                )
                                )
                            ]
                        )
                    ),

                    ft.Container(height=15),

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
                                    on_click=lambda e: self._ao_clicar_escolher_data(e, True)
                                ),

                                ft.Text(value='até', font_family='nunito-bold'),

                                ft.Container(
                                    padding=ft.padding.only(right=self._padding_padrao, left=self._padding_padrao),
                                    border_radius=12, width=150, height=40, alignment=ft.alignment.center,
                                    border=ft.Border(ft.BorderSide(1, '#222222'), ft.BorderSide(1, '#222222'),
                                                     ft.BorderSide(1, '#222222'), ft.BorderSide(1, '#222222')),
                                    content=self.texto_data_final,
                                    on_click=lambda e: self._ao_clicar_escolher_data(e, False)
                                ),
                            ]
                        )
                    )
                ]
            )
        )

        return bs

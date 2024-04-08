import flet as ft


class ChipStatusConsulta:
    def __init__(self, pagina: ft.Page, label: str, icone: str, cor_icone: str, funcao_ao_clicar):
        self.pagina = pagina
        self.label = label
        self.icone = icone
        self.cor_icone = cor_icone
        self.funcao_ao_clicar = funcao_ao_clicar
        self.get = self._get()

    def mudar_cor_ao_ser_selecionado(self, controle: ft.Chip):
        if controle.selected:
            controle.label_style = ft.TextStyle(
                color='#FFFFFF',
                font_family='nunito-regular'
            )

    def teste(self, e: ft.ControlEvent):
        self.mudar_cor_ao_ser_selecionado(e.control)
        self.pagina.update()

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
            on_select=lambda e: self.funcao_ao_clicar()
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
        self.get = self._get()

    def _get(self) -> ft.BottomSheet:
        bs = ft.BottomSheet(
            enable_drag=True,
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

                    ft.Container(height=20),

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
                    )
                ]
            )
        )

        return bs

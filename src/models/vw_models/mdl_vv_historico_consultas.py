import flet as ft
from src.views.view_historico_consultas.vwc_selecao_filtros import CardFiltrosDeConsultas


class BotaoFiltro:
    def __init__(self, page: ft.Page):
        self.pagina = page
        self.icone_filtro = ft.icons.FILTER_NONE_ROUNDED
        self.qntd_filtro = 0
        self.card_filtro_de_consultas = CardFiltrosDeConsultas(page)

        self.filtros_icones = {
            0: ft.icons.FILTER_NONE_ROUNDED,
            1: ft.icons.FILTER_1_ROUNDED,
            2: ft.icons.FILTER_2_ROUNDED,
            3: ft.icons.FILTER_3_ROUNDED,
            4: ft.icons.FILTER_4_ROUNDED,
            5: ft.icons.FILTER_5_ROUNDED,
            6: ft.icons.FILTER_6_ROUNDED,
            7: ft.icons.FILTER_7_ROUNDED,
            8: ft.icons.FILTER_8_ROUNDED,
            9: ft.icons.FILTER_9_ROUNDED,
        }

        self.get = self._get()

    def _get(self) -> ft.IconButton:
        btn = ft.IconButton(
            icon=self.filtros_icones[self.qntd_filtro],
            icon_color='#0BAB7D',
            on_click=lambda e: self._ao_clicar()
        )

        return btn

    def _ao_clicar(self):
        self.pagina.overlay.append(self.card_filtro_de_consultas.get)
        self.pagina.overlay[0].open = True
        self.pagina.overlay[0].update()

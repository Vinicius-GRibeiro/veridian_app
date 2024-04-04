import flet as ft
from src.views import vw_carteirinha, vw_conta, vw_inicio, vw_historico_consultas, vw_nova_consulta


class BotaoMenu:
    def __init__(self, icone: str):
        self._icone = icone
        self.get = self._get_botao()

    def _get_botao(self) -> ft.NavigationDestination:
        return ft.NavigationDestination(
            icon_content=ft.Icon(name=f'{self._icone}_OUTLINED', color=ft.colors.ON_SECONDARY_CONTAINER),
            selected_icon_content=ft.Icon(name=f'{self._icone}_ROUNDED', color=ft.colors.ON_SECONDARY_CONTAINER),
        )


class CtrlMenu:
    def __init__(self, pagina: ft.Page):
        self.pagina = pagina
        self.get = self._get_menu()

    def _get_menu(self) -> ft.NavigationBar:
        return ft.NavigationBar(
            bgcolor=ft.colors.SURFACE,
            selected_index=0,
            destinations=[
                BotaoMenu(icone='HOME').get, BotaoMenu(icone='ARTICLE').get, BotaoMenu(icone='ADD_CIRCLE').get,
                BotaoMenu(icone='BADGE').get, BotaoMenu(icone='PERSON').get
            ],
            on_change=lambda e: self._ao_mudar(e)
        )

    def _ao_mudar(self, e: ft.ControlEvent):
        indice_pagina = e.control.selected_index

        if indice_pagina == 0:
            self.pagina.clean()
            self.pagina.add(vw_inicio.Inicio(self.pagina).get_view)
        elif indice_pagina == 1:
            self.pagina.clean()
            self.pagina.add(vw_historico_consultas.HistoricoConsultas().get_view)
        elif indice_pagina == 2:
            self.pagina.clean()
            self.pagina.add(vw_nova_consulta.NovaConsulta().get_view)
        elif indice_pagina == 3:
            self.pagina.clean()
            self.pagina.add(vw_carteirinha.Carteirinha().get_view)
        elif indice_pagina == 4:
            self.pagina.clean()
            self.pagina.add(vw_conta.Conta().get_view)

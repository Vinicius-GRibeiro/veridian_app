import flet as ft
from src.views.view_nova_consulta import vw_nova_consulta
from src.views.view_conta import vw_conta
from src.views.view_carteirinha import vw_carteirinha
from src.views.view_historico_consultas import vw_main_historico_consultas
from src.views.view_inicio import vw_main_inicio


class BotaoMenu:
    def __init__(self, icone: str):
        self._icone = icone
        self.get = self._get_botao()

    def _get_botao(self) -> ft.NavigationDestination:
        return ft.NavigationDestination(
            icon_content=ft.Icon(name=f'{self._icone}_ROUNDED', color='#646F67'),
            selected_icon_content=ft.Icon(name=f'{self._icone}_ROUNDED', color='#EFFDF6'),
        )


class CtrlMenu:
    def __init__(self, pagina: ft.Page):
        self.pagina = pagina
        self.get = self._get_menu()

    def _get_menu(self) -> ft.NavigationBar:
        return ft.NavigationBar(
            bgcolor='#F2F2E8',
            indicator_color='#0BAB7D',
            indicator_shape=ft.RoundedRectangleBorder(radius=15),
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
            self.pagina.add(vw_main_inicio.Inicio(self.pagina).get_view)
        elif indice_pagina == 1:
            self.pagina.clean()
            self.pagina.add(vw_main_historico_consultas.HistoricoConsultas(self.pagina).get_view)
        elif indice_pagina == 2:
            self.pagina.clean()
            self.pagina.add(vw_nova_consulta.NovaConsulta().get_view)
        elif indice_pagina == 3:
            self.pagina.clean()
            self.pagina.add(vw_carteirinha.Carteirinha().get_view)
        elif indice_pagina == 4:
            self.pagina.clean()
            self.pagina.add(vw_conta.Conta().get_view)

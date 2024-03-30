import flet as ft
from ..models.ctrl_menu import CtrlMenu
from .inicio import Inicio


class Login:
    def __init__(self, pagina: ft.Page):
        self.pagina = pagina
        self.get_view = self._get_view()

    def _mudar(self):
        self.pagina.clean()
        self.pagina.navigation_bar = CtrlMenu(self.pagina).get
        self.pagina.add(Inicio(self.pagina).get_view)
        self.pagina.update()

    def _get_view(self) -> ft.Column:
        view = ft.Column(
            controls=[
                ft.ElevatedButton(text='logar', on_click=lambda e: self._mudar())
            ]
        )

        return view

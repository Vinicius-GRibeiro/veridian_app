import flet as ft


class Inicio:
    def __init__(self, pagina: ft.Page):
        self.pagina = pagina
        self.get_view = self._get_view()

    def _get_view(self) -> ft.Column:
        view = ft.Column(
            controls=[
                ft.Text('inicio')
            ]
        )

        return view

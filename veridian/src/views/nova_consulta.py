import flet as ft


class NovaConsulta:
    def __init__(self):
        self.get_view = self._get_view()

    def _get_view(self) -> ft.Column:
        view = ft.Column(
            controls=[
                ft.Text('nova consulta')
            ]
        )

        return view

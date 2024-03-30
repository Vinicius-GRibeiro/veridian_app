import flet as ft


class Conta:
    def __init__(self):
        self.get_view = self._get_view()

    def _get_view(self) -> ft.Column:
        view = ft.Column(
            controls=[
                ft.Text('Conta')
            ]
        )

        return view

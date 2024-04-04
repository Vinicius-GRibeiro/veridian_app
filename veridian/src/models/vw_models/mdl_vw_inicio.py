import flet as ft


class BotaoIcone:
    def __init__(self, icone: str):
        self.icone = icone
        self.get = self._get()

    def _get(self) -> ft.IconButton:
        btn = ft.IconButton(
            icon=self.icone,
            icon_color=ft.colors.ON_PRIMARY,
            icon_size=100
        )

        return btn

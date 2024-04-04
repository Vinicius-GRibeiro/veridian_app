import flet as ft
from src.controllers.ctrl_usuarios import Usuario


class Cabecalho:
    def __init__(self, pagina: ft.Page):
        self.pagina = pagina
        self.src_img = Usuario.buscar(colunas='img', condicao=f"cpf = '{self.pagina.session.get('user_id')}'")[0]
        self.nome_usuario = Usuario.buscar(colunas='nome', condicao=f"cpf = '{self.pagina.session.get('user_id')}'")[0]
        self.primeira_inicial, self.segunda_inicial = self.nome_usuario.split()[0][0], self.nome_usuario.split()[-1][0]

        self.get = self._get()

    def _get(self) -> ft.AppBar:
        bar = ft.AppBar(
            toolbar_height=50,
            leading_width=40,
            leading=ft.Container(
                padding=ft.padding.only(left=10),
                content=ft.CircleAvatar(
                    foreground_image_url=self.src_img,
                    content=ft.Text(value=f"{self.primeira_inicial}{self.segunda_inicial}", size=15,
                                    font_family='robotoregular'),

                ),
            ),
            actions=[
                ft.IconButton(icon=ft.icons.SEARCH ,icon_color=ft.colors.ON_PRIMARY)
            ],
            bgcolor=ft.colors.with_opacity(opacity=.9, color=ft.colors.ON_SECONDARY_CONTAINER),

        )

        return bar

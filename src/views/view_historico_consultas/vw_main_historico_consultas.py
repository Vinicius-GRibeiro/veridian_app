import flet as ft
from src.models.vw_models.mdl_vv_historico_consultas import BotaoFiltro


class HistoricoConsultas:
    def __init__(self, page: ft.Page):
        self.pagina = page
        self.botao_filtro = BotaoFiltro(page)
        self.get_view = self._get_view()

    def _get_view(self) -> ft.Column:
        view = ft.Column(
            spacing=0,
            controls=[
                ft.Container(
                    height=50,
                    bgcolor='#F2F2E8',
                    content=ft.Row(
                        spacing=0,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Container(
                                padding=ft.padding.only(left=20),
                                content=ft.Text(value='Histórico de consultas', font_family='nunito-bold',
                                                color='#646F67'),
                            ),

                            ft.Container(
                                padding=ft.padding.only(right=20),
                                content=self.botao_filtro.get
                            )
                        ]
                    )
                ),


            ]
        )

        return view

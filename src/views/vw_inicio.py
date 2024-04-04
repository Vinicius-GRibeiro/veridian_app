import flet as ft
from src.models.vw_models.mdl_vw_inicio import BotaoIcone


class Inicio:
    def __init__(self, pagina: ft.Page):
        self.botao_exames = BotaoIcone(icone=ft.icons.BIOTECH_ROUNDED)
        self.botao_receitas = BotaoIcone(icone=ft.icons.LIST_ALT_ROUNDED)
        self.botao_clinicas = BotaoIcone(icone=ft.icons.PLACE_ROUNDED)

        self.valor_offset = 1
        self.pagina = pagina
        self.get_view = self._get_view()

    def _get_view(self) -> ft.Column:
        view = ft.Column(
            controls=[
                ft.ResponsiveRow(
                    controls=[
                        ft.Container(
                            padding=ft.padding.only(top=40, bottom=20),
                            alignment=ft.alignment.center,
                            content=ft.Row(
                                spacing=20,
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                bgcolor=ft.colors.ON_BACKGROUND,
                                                content=self.botao_exames.get,
                                                border_radius=20,
                                                shadow=ft.BoxShadow(
                                                    offset=ft.Offset(x=self.valor_offset, y=self.valor_offset),
                                                    color=ft.colors.SHADOW,
                                                    spread_radius=2,
                                                    blur_radius=7
                                                )
                                            ),

                                            ft.Text(
                                                value='EXAMES',
                                                size=15,
                                                color=ft.colors.ON_SECONDARY_CONTAINER,
                                                font_family='robotoblack'
                                            )
                                        ]
                                    ),

                                    ft.Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                bgcolor=ft.colors.SECONDARY,
                                                content=self.botao_receitas.get,
                                                border_radius=20,
                                                shadow=ft.BoxShadow(
                                                    offset=ft.Offset(x=self.valor_offset, y=self.valor_offset),
                                                    color=ft.colors.SHADOW,
                                                    spread_radius=2,
                                                    blur_radius=7
                                                )
                                            ),

                                            ft.Text(
                                                value='RECEITAS',
                                                size=15,
                                                color=ft.colors.ON_SECONDARY_CONTAINER,
                                                font_family='robotoblack'
                                            )
                                        ]
                                    ),

                                    ft.Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                bgcolor=ft.colors.TERTIARY,
                                                content=self.botao_clinicas.get,
                                                border_radius=20,
                                                shadow=ft.BoxShadow(
                                                    offset=ft.Offset(x=self.valor_offset, y=self.valor_offset),
                                                    color=ft.colors.SHADOW,
                                                    spread_radius=2,
                                                    blur_radius=7
                                                )
                                            ),

                                            ft.Text(
                                                value='CLÍNICAS',
                                                size=15,
                                                color=ft.colors.ON_SECONDARY_CONTAINER,
                                                font_family='robotoblack'
                                            )
                                        ]
                                    )
                                ]
                            )
                        )
                    ]
                ),

                ft.Container(
                    bgcolor=ft.colors.with_opacity(opacity=.5, color=ft.colors.ON_SECONDARY_CONTAINER),
                    height=.5
                )
            ]
        )

        return view

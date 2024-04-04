import flet as ft
from src.models.vw_models.mdl_vw_login import CaixaDeTexto, BotaoTexto, BotaoComum


class Login:
    def __init__(self, pagina: ft.Page):
        self.pagina = pagina
        self.caixa_cpf = CaixaDeTexto(label='E-mail')
        self.caixa_senha = CaixaDeTexto(label='Senha', is_senha=True)
        self.btn_esqueci_a_senha = BotaoTexto(texto='esqueci a senha')
        self.btn_entrar = BotaoComum(texto='entrar', caixa_cpf=self.caixa_cpf, caixa_senha=self.caixa_senha,
                                     pagina=self.pagina)
        self.btn_entre_em_contato = ft.Text(value='Entre em contato', font_family='robotolight',
                                            color=ft.colors.ON_PRIMARY, size=16, weight=ft.FontWeight.BOLD, )

        self.get_view = self._get_view()

    def _get_view(self) -> ft.Column:
        view = ft.Column(
            spacing=0,
            expand=True,
            controls=[
                ft.Container(
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=['#05201C', '#006A60']
                    ),
                    expand=True,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Column(
                                spacing=0,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Container(
                                        padding=ft.padding.only(top=50),
                                        width=280,
                                        content=ft.Image(src='img/logo_cropped3.png'),
                                    ),

                                    ft.Container(
                                        padding=ft.padding.only(top=50),
                                        content=ft.Text(
                                            value='Entre na sua conta',
                                            font_family='robotolight',
                                            size=25,
                                            color=ft.colors.ON_PRIMARY
                                        )
                                    ),

                                    ft.Container(
                                        padding=ft.padding.only(top=50),
                                        content=self.caixa_cpf.get
                                    ),

                                    ft.Container(
                                        padding=ft.padding.only(top=10),
                                        content=self.caixa_senha.get
                                    ),

                                    ft.Container(
                                        width=300,
                                        alignment=ft.alignment.center_right,
                                        content=self.btn_esqueci_a_senha.get,
                                        padding=ft.padding.only(bottom=30)
                                    ),

                                    ft.Container(
                                        width=170,
                                        height=40,
                                        border_radius=20,
                                        gradient=ft.LinearGradient(
                                            begin=ft.alignment.center_left,
                                            end=ft.alignment.center_right,
                                            colors=['#0E3C7D', '#196DE3']
                                        ),
                                        content=self.btn_entrar.get
                                    ),

                                    ft.Container(
                                        padding=ft.padding.only(top=30, bottom=30),
                                        content=ft.Container(
                                            bgcolor=ft.colors.ON_PRIMARY,
                                            height=.5,
                                            width=300
                                        )
                                    ),

                                    ft.Container(
                                        content=ft.Text(value='Ainda não tem uma conta?', font_family='robotolight',
                                                        color=ft.colors.ON_PRIMARY, size=16)
                                    ),

                                    ft.Container(
                                        content=self.btn_entre_em_contato,
                                        on_click=lambda e: print('clicado'),
                                    )
                                ]
                            )
                        ]
                    )
                )
            ]
        )

        return view

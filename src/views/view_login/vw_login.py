import flet as ft
from src.models.vw_models.mdl_vw_login import CaixaDeTexto, BotaoTexto, BotaoComum


class Login:
    def __init__(self, pagina: ft.Page):
        self.pagina = pagina
        self.caixa_cpf = CaixaDeTexto(label='Informe seu endereço de e-mail', icone=ft.icons.EMAIL_OUTLINED)
        self.caixa_senha = CaixaDeTexto(label='Informe sua senha', is_senha=True, icone=ft.icons.LOCK_OUTLINE)

        self.btn_esqueci_a_senha = BotaoTexto(texto='Esqueceu sua senha?')

        self.btn_entrar = BotaoComum(texto='Entrar', caixa_cpf=self.caixa_cpf, caixa_senha=self.caixa_senha,
                                     pagina=self.pagina)

        self.btn_criar_conta = ft.Text(value='Não tem uma conta? Crie agora', font_family='robotolight',
                                       color=ft.colors.ON_PRIMARY, size=16, weight=ft.FontWeight.BOLD, )

        self.get_view = self._get_view()

    def _get_view(self) -> ft.Column:
        view = ft.Column(
            spacing=0,
            controls=[
                ft.Row(
                    spacing=0,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            alignment=ft.alignment.center,
                            expand=True,
                            bgcolor='#1D212D',
                            height=150,
                            border_radius=ft.BorderRadius(bottom_left=600, bottom_right=600, top_right=0, top_left=0),
                            content=ft.Column(
                                spacing=0,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Container(height=15),
                                    ft.Text(value='Veridian', font_family='nunito-xbold', color='#09BA86', size=40),
                                    ft.Text(value='Entre na sua conta Veridian', font_family='nunito-light',
                                            color='#FFFFFF', size=15),
                                ]
                            )
                        ),
                    ]
                ),

                ft.Container(height=50),

                ft.Row(
                    spacing=0,
                    controls=[
                        ft.Container(
                            expand=True,
                            alignment=ft.alignment.center,
                            content=ft.Column(
                                spacing=2,
                                controls=[
                                    ft.Text(value='E-mail', font_family='nunito-xbold'),
                                    self.caixa_cpf.get
                                ]
                            )
                        )
                    ]
                ),

                ft.Container(height=25),

                ft.Row(
                    spacing=0,
                    controls=[
                        ft.Container(
                            expand=True,
                            alignment=ft.alignment.center,
                            content=ft.Column(
                                spacing=0,
                                controls=[
                                    ft.Text(value='Senha', font_family='nunito-xbold'),
                                    self.caixa_senha.get
                                ]
                            )
                        )
                    ]
                ),

                ft.Container(height=50),

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        self.btn_entrar.get
                    ]
                ),

                ft.Container(height=30),

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(width=120, bgcolor='#BDBDBD', height=1.5),
                        ft.Text(value='ou', font_family='nunito-regular', color='#555555', weight=ft.FontWeight.BOLD),
                        ft.Container(width=120, bgcolor='#BDBDBD', height=1.5)
                    ]
                ),

                ft.Container(height=20),

                ft.Column(
                    controls=[
                        ft.Row(
                            spacing=5,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Text(value='Ainda não tem uma conta?', font_family='nunito-semibold',
                                        color='#424242'),
                                ft.Text(value='Crie agora', font_family='nunito-semibold',
                                        color='#424242', weight=ft.FontWeight.W_800)
                            ]
                        ),

                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Text(value='Esqueceu sua senha?', color='#0BAB7C', font_family='nunito-semibold',
                                        weight=ft.FontWeight.BOLD)
                            ]
                        )
                    ]
                )
            ]
        )

        return view

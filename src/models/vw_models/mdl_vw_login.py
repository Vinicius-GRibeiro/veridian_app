import flet as ft
from src.controllers.ctrl_utils import mostrar_notificacao
from src.controllers.ctrl_credenciais import Credencial, gerar_hash, comparar_hash
from src.views.componentes_compartilhados.vwc_menu import CtrlMenu
from src.views.view_inicio.vw_main_inicio import Inicio


class CaixaDeTexto:
    def __init__(self, label: str, icone: str, is_senha: bool = False):
        self.label = label
        self.icone = icone
        self.is_senha = is_senha
        self.get = self._get()

    def _get(self) -> ft.TextField:
        caixa = ft.TextField(
            hint_text=self.label,
            border_color='transparent',
            border_radius=16,
            password=self.is_senha,
            bgcolor='#F3F2E9',
            width=300,
            prefix_icon=self.icone,
            can_reveal_password=True if self.is_senha else None,
            text_style=ft.TextStyle(
                font_family='nunito-semibold',
                color='#424242'
            ),
        )

        return caixa


class BotaoTexto:
    def __init__(self, texto: str, tamanho: int = 20):
        self.texto = texto
        self.tamanho = tamanho
        self.get = self._get()

    def _get(self) -> ft.TextButton:
        btn = ft.TextButton(
            content=ft.Text(value=self.texto, color=ft.colors.ON_PRIMARY, font_family='robotothin'),
        )

        return btn


class BotaoComum:
    def __init__(self, pagina: ft.Page, texto: str, caixa_cpf: CaixaDeTexto, caixa_senha: CaixaDeTexto):
        self.pagina = pagina
        self.texto = texto
        self.caixa_cpf = caixa_cpf
        self.caixa_senha = caixa_senha
        self.get = self._get()

    def _get(self) -> ft.FilledButton:
        btn = ft.FilledButton(
            width=300,
            height=50,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Text(value=self.texto, color='#FBFAF3', font_family='nunito-xbold', size=15),
                    ft.Icon(name=ft.icons.ARROW_FORWARD_ROUNDED, color='#FBFAF3')
                ]
            ),
            style=ft.ButtonStyle(
                overlay_color='transparent',
                bgcolor='#0BAB7C',
                shape=ft.RoundedRectangleBorder(radius=12)
            ),
            on_click=lambda e: self._ao_clicar(e)
        )

        return btn

    def _ao_clicar(self, e):
        if self.caixa_cpf.get.value != '' and self.caixa_senha.get.value != '':
            emails = Credencial.buscar(colunas='login')

            email_informado = self.caixa_cpf.get.value
            senha_informada = self.caixa_senha.get.value

            hash_senha_informada = gerar_hash(senha_informada)

            if email_informado in emails:
                hash_senha_cadastrada = Credencial.buscar(colunas='senha', condicao=f"login = '{email_informado}'")

                if comparar_hash(h1=hash_senha_informada, h2=hash_senha_cadastrada[0]):
                    self.pagina.clean()
                    self.pagina.navigation_bar = CtrlMenu(self.pagina).get
                    self.pagina.add(Inicio(self.pagina).get_view)
                    self.pagina.update()
                    return
            mostrar_notificacao(pagina=self.pagina, mensagem='E-mail ou senha inválidos. Verifique e tente novamente')
            self.caixa_senha.get.value = ''
            self.pagina.update()
        else:
            mostrar_notificacao(pagina=self.pagina, mensagem='Preencha o e-mail e a sua senha Veridian')

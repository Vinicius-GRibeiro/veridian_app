import flet as ft
from src.controllers.ctrl_utils import mostrar_notificacao
from src.controllers.ctrl_credenciais import Credencial, gerar_hash, comparar_hash
from src.controllers.ctrl_menu import CtrlMenu
from src.views.vw_inicio import Inicio


class CaixaDeTexto:
    def __init__(self, label: str, is_senha: bool = False):
        self.label = label
        self.is_senha = is_senha
        self.get = self._get()

    def _get(self) -> ft.TextField:
        caixa = ft.TextField(
            label=self.label,
            border_color=ft.colors.ON_PRIMARY,
            focused_border_color=ft.colors.ON_PRIMARY,
            password=self.is_senha,
            can_reveal_password=True if self.is_senha else None,
            text_style=ft.TextStyle(
                font_family='robotothin',
                color=ft.colors.ON_PRIMARY
            ),
            label_style=ft.TextStyle(
                font_family='robotothin',
                color=ft.colors.ON_PRIMARY
            )
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
            width=150,
            content=ft.Text(value=self.texto, color=ft.colors.ON_PRIMARY, font_family='robotolight', size=20),
            style=ft.ButtonStyle(
                overlay_color='transparent',
                bgcolor='transparent',
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

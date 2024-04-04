import flet as ft
from screeninfo import get_monitors
from src.controllers.ctrl_utils import proporcao_celular
from src.views import vw_login, vw_inicio
from assets import fonts
from src.controllers.ctrl_menu import CtrlMenu
from src.controllers.ctrl_cabecalho import Cabecalho


AJUSTE_ALTURA_CELULAR = -50
altura_monitor, largura_monitor = get_monitors()[0].height, get_monitors()[0].width
altura_celular, largura_celular = proporcao_celular(altura_monitor, largura_monitor)


def main(page: ft.Page):
    #  Instanciando a tela de login
    # view_login = vw_login.Login(page)  # 0
    view_inicio = vw_inicio.Inicio(page)

    #  Definindo as fontes do projeto
    page.fonts = fonts.fonts

    # Definindo projeto para android
    page.platform = ft.PagePlatform.ANDROID

    # Especificações de estilo
    page.padding = 0
    page.spacing = 0
    page.theme = ft.theme.Theme(color_scheme_seed=ft.colors.TEAL)
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.SURFACE_VARIANT
    page.window_width = largura_celular
    page.window_height = altura_celular + AJUSTE_ALTURA_CELULAR

    #  Armazenando nas variávis de sessão, os valores de altura e largura definidos
    page.session.set('altura-tela', altura_celular+AJUSTE_ALTURA_CELULAR)
    page.session.set('largura-tela', largura_celular)

    # Definições de inicialização da janela
    page.window_top = True
    page.window_center = True

    # TODO: REMOVER CPF E INCREMENTAR VARIÁVEL DE SESSÃO NO LOGIN
    page.session.set('user_id', '53406890857')

    # TODO: REMOVER MENU
    page.navigation_bar = CtrlMenu(page).get

    # TODO: REMOVER CABEÇALHO
    page.appbar = Cabecalho(page).get

    #TODO: TROCAR VIEW INICIAL
    #  View inicial
    # page.add(view_login.get_view)
    page.add(view_inicio.get_view)


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')

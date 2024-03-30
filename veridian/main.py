import flet as ft
from screeninfo import get_monitors
from src.controllers.utils import proporcao_celular
from src.views import login


AJUSTE_ALTURA_CELULAR = -50
altura_monitor, largura_monitor = get_monitors()[0].height, get_monitors()[0].width
altura_celular, largura_celular = proporcao_celular(altura_monitor, largura_monitor)


def main(page: ft.Page):
    view_login = login.Login(page)  # 0

    # Definindo projeto para android
    page.platform = ft.PagePlatform.ANDROID

    # Especificações de estilo
    page.theme = ft.theme.Theme(color_scheme_seed=ft.colors.TEAL)
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.SURFACE_VARIANT
    page.window_width = largura_celular
    page.window_height = altura_celular + AJUSTE_ALTURA_CELULAR

    # Definições de inicialização da janela
    page.window_top = True
    page.window_center = True

    page.add(view_login.get_view)



ft.app(target=main)

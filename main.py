import flet as ft
from assets import fonts
from screeninfo import get_monitors
from src.controllers.ctrl_utils import proporcao_celular
from src.views.componentes_compartilhados.vwc_menu import CtrlMenu
from src.views.view_historico_consultas.vw_main_historico_consultas import HistoricoConsultas
from src.views.view_historico_consultas.vwc_selecao_filtros import CardFiltrosDeConsultas, CalendarioFiltroDeConsulta


AJUSTE_ALTURA_CELULAR = -50
altura_monitor, largura_monitor = get_monitors()[0].height, get_monitors()[0].width
altura_celular, largura_celular = proporcao_celular(altura_monitor, largura_monitor)


def main(page: ft.Page):
    # TODO: REMOVER CPF E INCREMENTAR VARIÁVEL DE SESSÃO NO LOGIN
    page.session.set('user_cpf', '08604635165')

    page.session.set('data_final_inicial', 'inicial')

    # Adição de componentes de overlay
    # Estes componentes devem ser adicionados nessa exata ordem
    page.overlay.append(CardFiltrosDeConsultas(page).get)
    page.overlay.append(CalendarioFiltroDeConsulta(page).get)

    #  Instanciando a tela de login
    # view_inicio = vw_inicio.Inicio(page)
    # view_login = Login(page)  # 0
    view_historico = HistoricoConsultas(page)

    #  Definindo as fontes do projeto
    page.fonts = fonts.fonts

    # Definindo projeto para android
    page.platform = ft.PagePlatform.ANDROID

    # Especificações de estilo
    page.padding = 0
    page.spacing = 0
    page.theme = ft.theme.Theme(color_scheme_seed=ft.colors.TEAL)
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = '#FBFAF3'
    page.window_width = largura_celular
    page.window_height = altura_celular + AJUSTE_ALTURA_CELULAR

    #  Armazenando nas variávis de sessão, os valores de altura e largura definidos
    page.session.set('altura-tela', altura_celular+AJUSTE_ALTURA_CELULAR)
    page.session.set('largura-tela', largura_celular)

    # Definições de inicialização da janela
    page.window_top = True
    page.window_center = True

    # TODO: REMOVER MENU
    page.navigation_bar = CtrlMenu(page).get

    # TODO: TROCAR VIEW INICIAL
    # page.add(view_login.get_view)
    # page.add(view_inicio.get_view)
    page.add(view_historico.get_view)

    # TODO: REMOVER ABERTURA DE OVERLAY DE FILTROS HARDCODED
    page.overlay[0].open = True
    page.overlay[0].update()


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')

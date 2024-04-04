import flet as ft


def proporcao_celular(altura_monitor, largura_monitor):
    proporcao = 16 / 9
    if altura_monitor < largura_monitor * proporcao:
        altura_celular = altura_monitor
        largura_celular = altura_monitor / proporcao
    else:
        largura_celular = largura_monitor
        altura_celular = largura_monitor * proporcao
    return altura_celular, largura_celular


def mostrar_notificacao(pagina: ft.Page, mensagem: str):
    notificacao = ft.SnackBar(
        bgcolor=ft.colors.ON_PRIMARY_CONTAINER,
        content=ft.Text(value=mensagem, color=ft.colors.ON_PRIMARY),
    )

    pagina.snack_bar = notificacao
    pagina.snack_bar.open = True
    pagina.update()

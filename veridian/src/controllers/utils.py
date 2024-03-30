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


# def rotas(page: ft.Page, views: list):
#     view_login = views[0]
#     view_inicio = views[1]
#     view_historico_de_consultas = views[2]
#     view_nova_consulta = views[3]
#     view_carteirinha = views[4]
#     view_conta = views[5]
#
#     def route_change(route):
#         page.views.clear()
#         page.views.append(view_login.get_view)
#
#         match page.route:
#             case '/':
#                 page.views.append(view_login.get_view)
#             case '/inicio':
#                 page.views.append(view_inicio.get_view)
#             case '/historico_consultas':
#                 page.views.append(view_historico_de_consultas.get_view)
#             case '/nova_consulta':
#                 page.views.append(view_nova_consulta.get_view)
#             case '/carteirinha':
#                 page.views.append(view_carteirinha.get_view)
#             case '/conta':
#                 page.views.append(view_conta.get_view)
#
#         page.update()
#
#     def view_pop(view):
#         page.views.pop()
#         top_view = page.views[-1]
#         page.go(top_view.route)
#
#     page.on_route_change = route_change
#     page.on_view_pop = view_pop
#     page.go(page.route)

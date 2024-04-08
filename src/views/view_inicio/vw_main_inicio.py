import flet as ft
from src.controllers.ctrl_usuarios import Usuario
from src.controllers.ctrl_consultas import Consulta
from src.controllers.ctrl_medico import Medico
from src.controllers.ctrl_data_horario import converter_timestamp
from src.models.vw_models.mdl_vw_inicio import CaixaDeTexto, CartaoDeInformacaoClinicasProximas, CartaoConsultas


class Inicio:
    def __init__(self, pagina: ft.Page):
        self.pagina = pagina
        self.pagina.bgcolor = '#FBFBF3'
        self.pagina.update()

        self.user_cpf = self.pagina.session.get('user_cpf')

        self.USER_ALL_DATA = Usuario.buscar(colunas='nome, img', condicao=f"cpf = '{self.user_cpf}'")

        self.user_fullname = self.USER_ALL_DATA[0][0]
        self.user_shortname = f"{self.user_fullname.split()[0]} {self.user_fullname.split()[-1]}"
        self.user_iniciais = self.user_shortname.split()[0][0] + self.user_shortname.split()[-1][0]
        self.user_profile_img_url = self.USER_ALL_DATA[0][1]

        self.caixa_de_pesquisa = CaixaDeTexto(dica='Procure por especialistas', icone_sufixo=ft.icons.SEARCH)

        self.card_clinicas_proximas = CartaoDeInformacaoClinicasProximas()

        self.consultas = Consulta.buscar(condicao=f"cpf_paciente = '{self.user_cpf}'")
        self.consultas_estruturado = []

        for i in self.consultas:
            id_consulta = i[0]
            cpf_medico = i[2]
            data_consulta = converter_timestamp(i[4])[0]
            hora_consulta = converter_timestamp(i[4])[1]
            status_consulta = i[3]

            especialidade_medico = Medico.buscar(colunas='especialidade', condicao=f"cpf_usuario = {cpf_medico}")[0][0]
            nome_medico, url_imagem_medico = Usuario.buscar(colunas='nome, img', condicao=f"cpf = '{cpf_medico}'")[0]

            if status_consulta == 'agendado':
                self.consultas_estruturado.append(
                    (id_consulta, nome_medico, especialidade_medico, data_consulta, hora_consulta, status_consulta,
                     url_imagem_medico)
                )

        self.linha_cartoes_consulta = ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[],
                                             scroll=ft.ScrollMode.AUTO)

        for consulta in self.consultas_estruturado:
            self.linha_cartoes_consulta.controls.append(
                CartaoConsultas(*consulta).get
            )

        self.get_view = self._get_view()

    def _get_view(self) -> ft.Column:
        view = ft.Column(
            spacing=0,
            controls=[

                ft.Container(height=20, bgcolor='#F2F2E8'),
                ft.Container(
                    bgcolor='#F2F2E8',
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        spacing=0,
                        controls=[
                            ft.Column(
                                spacing=0,
                                controls=[
                                    ft.Text(value=f'Olá, {self.user_shortname}', font_family='nunito-bold', size=20,
                                            color='#212121'),
                                    ft.Text(value=f'bem vindo(a)', font_family='nunito-regular', size=15,
                                            color='#647080', weight=ft.FontWeight.BOLD)
                                ]
                            ),

                            ft.Container(width=30),

                            ft.CircleAvatar(
                                foreground_image_url=self.user_profile_img_url,
                                content=ft.Text(value=self.user_iniciais, color='#FFFFFF',
                                                text_align=ft.TextAlign.CENTER),
                                bgcolor='#0BAB7D'
                            ),
                        ]
                    ),
                ),
                ft.Container(height=20, bgcolor='#F2F2E8',
                             border_radius=ft.BorderRadius(bottom_left=24, bottom_right=24, top_right=0, top_left=0)),

                ft.Container(height=20),

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=0,
                    controls=[
                        self.caixa_de_pesquisa.get
                    ]
                ),

                ft.Container(height=30),

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        self.card_clinicas_proximas.get
                    ]
                ),

                ft.Container(height=30),

                ft.Container(
                    content=ft.Text(value='Consultas próximas', font_family='nunito-bold', color='#212121', size=18),
                    padding=ft.padding.only(left=35, bottom=10)
                ),

                ft.Container(
                    padding=ft.padding.only(left=30, right=30),
                    content=self.linha_cartoes_consulta,
                )

            ]
        )

        return view

import flet as ft
from src.controllers.ctrl_data_horario import converter_timestamp, obter_param_especifico


class ContainerConsulta:
    def __init__(self, id_consulta, status, timestamp, especialidade, obs, crm, nome_medico, genero_medico,
                 imagem_medico):
        self.dia_numero = obter_param_especifico(timestamp, 'd')
        self.mes_short = obter_param_especifico(timestamp, 'b')
        self.ano = obter_param_especifico(timestamp, 'Y')
        self.hora = (converter_timestamp(timestamp)[1])

        self.id_consulta = id_consulta
        self.status = status
        self.especialidade = especialidade
        self.obs = obs if obs is not None else '-'
        self.crm = crm
        self.nome_medico_completo = nome_medico
        self.nome_medico = f"{nome_medico.split()[0]} {nome_medico.split()[-1]}"
        self.iniciais_medico = f"{nome_medico.split()[0][0]} {nome_medico.split()[-1][0]}"
        self.genero_medico = genero_medico
        self.pronome_tratamento = 'Dra.'if self.genero_medico == 'Feminino' else 'Dr.'
        self.imagem_medico = imagem_medico
        self.cor_status = '#A7FFEB' if self.status == 'realizado' else 'yellow' if self.status == 'agendado' else 'red'

        self._RAIO_BORDA = 16

        self.get = self._get()

    def _get(self) -> ft.Container:
        card = ft.Container(
            padding=ft.padding.only(left=10, right=10),
            content=ft.Container(
                border_radius=self._RAIO_BORDA,
                bgcolor='#C5E1A5',
                content=ft.Row(
                    spacing=0,
                    controls=[
                        ft.Container(
                            bgcolor='#0BAB7D',
                            border_radius=ft.BorderRadius(top_left=self._RAIO_BORDA, bottom_left=self._RAIO_BORDA,
                                                          top_right=0, bottom_right=0),
                            border=ft.Border(right=ft.BorderSide(width=1, color='white')),
                            content=ft.Container(
                                padding=15,
                                content=ft.Column(
                                    spacing=0,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(self.dia_numero, font_family='nunito-light', size=25, color='#ECF0F1'),
                                        ft.Text(self.mes_short.upper(), font_family='nunito-light', size=20,
                                                color='#ECF0F1', weight=ft.FontWeight.BOLD),
                                        ft.Text(self.ano, font_family='nunito-light', size=10, color='#ECF0F1')

                                    ]
                                )
                            )
                        ),

                        ft.Container(
                            expand=True,
                            padding=ft.padding.only(right=10, left=10),
                            content=ft.Column(
                                spacing=0,
                                controls=[
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        spacing=0,
                                        controls=[
                                            ft.Text(f"{self.pronome_tratamento} {self.nome_medico}",
                                                    font_family='nunito-bold', size=16),

                                            ft.Container(
                                                scale=.9,
                                                padding=5,
                                                border_radius=8,
                                                bgcolor='#0BAB7D',
                                                content=ft.Row(
                                                    controls=[
                                                        ft.Icon(name=ft.icons.CIRCLE, color=self.cor_status, size=10),

                                                        ft.Container(ft.Text(self.status, color='#ECF0F1',
                                                                             font_family='nunito-regular'))
                                                    ]
                                                )
                                            ),

                                        ]
                                    ),

                                    ft.Text(f"{self.especialidade.upper()} - CRM {self.crm}",
                                            font_family='nunito-regular', weight=ft.FontWeight.BOLD, size=12)
                                ]
                            )
                        ),



                    ]
                )
            )
        )

        return card
import flet as ft


class CaixaDeTexto:
    def __init__(self, dica: str, icone_sufixo: str, largura: int = 360):
        self.dica = dica
        self.icone_sufixo = icone_sufixo
        self.largura = largura
        self.get = self._get()

    def _get(self) -> ft.TextField:
        txt = ft.TextField(
            suffix_icon=self.icone_sufixo,
            suffix_style=ft.TextStyle(
                color='#ACADAC'
            ),
            hint_text=self.dica,
            bgcolor='#F2F2E8',
            text_style=ft.TextStyle(
                font_family='nunito-medium'
            ),
            hint_style=ft.TextStyle(
                font_family='nunito-medium',
                color='#ACADAC'
            ),
            border_color='transparent',
            border_radius=20,
            width=self.largura
        )

        return txt


class CartaoDeInformacaoClinicasProximas:
    def __init__(self):
        self.get = self._get()

    def _get(self) -> ft.Container:
        card = ft.Container(
            border_radius=20,
            padding=20,
            bgcolor='#C8F4C3',
            alignment=ft.alignment.center,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                width=320,
                spacing=0,
                controls=[
                    ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=0,
                        controls=[
                            ft.Text(value='Clínicas por perto', font_family='nunito-bold', color='#323234'),
                            ft.Text(value='Buscando clínicas perto de você?\nProcure uma agora',
                                    font_family='nunito-regular', color='#716F7B'),
                            ft.Container(height=20),
                            ft.FilledButton(content=ft.Text(value='BUSCAR', font_family='nunito-black',
                                                            color='#FFFFFF'), style=ft.ButtonStyle(
                                bgcolor='#0BAB7D'
                            ))
                        ]
                    ),

                    ft.Icon(
                        name=ft.icons.LOCAL_HOSPITAL_ROUNDED,
                        color='#0BAB7D',
                        size=80
                    )
                ]
            )
        )

        return card


class CartaoConsultas:
    def __init__(self, id_consulta, nome_medico: str, especialidade_medico: str, data_consulta: str, hora_consulta: str,
                 status_consulta: str, url_imagem_medico: str):
        self.id_consulta = id_consulta
        self.nome_medico = f"{nome_medico.split()[0]} {nome_medico.split()[-1]}"
        self.especialidade = especialidade_medico
        self.data_consulta = data_consulta
        self.hora_consulta = hora_consulta
        self.status_consulta = status_consulta
        self.user_image_urlm = url_imagem_medico
        self.cor_indicador = '#3AC199' if self.status_consulta == 'agendado' or self.status_consulta == 'realizado' else '#ED2E1C'
        self.get = self._get()

    def _get(self) -> ft.Container:
        card = ft.Container(
            key=self.id_consulta,
            border_radius=20,
            padding=20,
            bgcolor='#D8D0FF',
            alignment=ft.alignment.center,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                width=320,
                spacing=0,
                controls=[
                    ft.Container(
                        width=90,
                        height=110,
                        bgcolor='#6048E6',
                        border_radius=16,
                        padding=0,
                        content=ft.Image(
                            src=self.user_image_urlm,
                            expand=True,
                            fit=ft.ImageFit.COVER
                        )
                    ),

                    ft.Container(
                        width=220,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            spacing=0,
                            controls=[
                                ft.Text(value=f"Dr. {self.nome_medico}", color='#2B2B29', font_family='nunito-black',
                                        size=20),
                                ft.Text(value=f"{self.especialidade.capitalize()}", color='#7C7989',
                                        font_family='nunito-bold', size=17),

                                ft.Text(value=f"{self.data_consulta} - {self.hora_consulta}",
                                        font_family='nunito-regular', color='#7C7989', size=15),
                                ft.Container(height=10),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.END,
                                    controls=[
                                        ft.Container(
                                            padding=ft.padding.Padding(top=5, bottom=5, right=10, left=10),
                                            border_radius=16,
                                            content=ft.Text(value=self.status_consulta, font_family='nunito-regular',
                                                            color='#FFFFFF'),
                                            bgcolor=self.cor_indicador
                                        )
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )

        return card

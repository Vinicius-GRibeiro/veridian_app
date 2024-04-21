from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')


def gerar_timestamp(data, hora="00:00"):
    formato_data = "%d/%m/%Y"
    formato_hora = "%H:%M"

    data_hora_str = f"{data} {hora}"
    data_hora_obj = datetime.strptime(data_hora_str, f"{formato_data} {formato_hora}")

    timestamp = int(data_hora_obj.timestamp())

    return timestamp


def converter_timestamp(timestamp):
    data_hora_obj = datetime.fromtimestamp(timestamp)
    data_hora_formatada = data_hora_obj.strftime("%d/%m/%Y %H:%M")

    return data_hora_formatada.split()


def obter_param_especifico(timestamp, formato: str = 'A'):
    data_hora_obj = datetime.fromtimestamp(timestamp)
    info = data_hora_obj.strftime(f'%{formato}')
    return info


def formatar_dd_mm_aaaa(data):
    data_formatada = datetime.strptime(data, '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y')
    return data_formatada

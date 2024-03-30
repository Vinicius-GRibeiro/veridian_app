import hashlib


def gerar_hash(texto_plano: str):
    return hashlib.sha256(texto_plano.encode()).hexdigest()


def comparar_hash(valor1: str, valor2: str, is_val1_hash: bool = False, is_val2_hash: bool = False):
    resultado = None

    if is_val1_hash:
        resultado = (valor1 == valor2) if is_val2_hash else (valor1 == gerar_hash(valor2))
    else:
        resultado = (gerar_hash(valor1) == valor2) if is_val2_hash else (gerar_hash(valor1) == gerar_hash(valor2))

    return resultado

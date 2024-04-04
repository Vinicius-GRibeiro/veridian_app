import hashlib


def gerar_hash(texto_plano: str):
    return hashlib.sha256(texto_plano.encode()).hexdigest()


def comparar_hash(h1: str, h2: str):
    return h1 == h2

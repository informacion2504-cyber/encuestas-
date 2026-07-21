import pandas as pd
import unicodedata
from core.reglas import *

def normalizar_texto(texto):

    texto = str(texto).strip().lower()

    texto = ''.join(
        c for c in unicodedata.normalize("NFD", texto)
        if unicodedata.category(c) != "Mn"
    )

    return texto


def calcular_satisfaccion(df, columna):

    respuestas = df[columna].dropna()

    if len(respuestas) == 0:
        return 0

    total = len(respuestas)

    respuestas_normalizadas = respuestas.apply(normalizar_texto)

    favorables_normalizadas = [
        normalizar_texto(r)
        for r in SATISFACCION_FAVORABLE
    ]

    favorables = respuestas_normalizadas.isin(
        favorables_normalizadas
    ).sum()

    porcentaje = round(
        (favorables / total) * 100,
        1
    )

    return porcentaje


def calcular_recomendacion(df, columna):

    respuestas = df[columna].dropna()

    if len(respuestas) == 0:
        return 0

    total = len(respuestas)

    respuestas_normalizadas = respuestas.apply(normalizar_texto)

    favorables_normalizadas = [
        normalizar_texto(r)
        for r in RECOMENDACION_FAVORABLE
]

    favorables = respuestas_normalizadas.isin(
        favorables_normalizadas
    ).sum()

    porcentaje = round(
        (favorables / total) * 100,
        1
    )

    return porcentaje
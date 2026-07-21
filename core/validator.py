import re


def normalizar(texto):
    """
    Normaliza un texto para facilitar comparaciones.
    """

    texto = str(texto).lower().strip()

    texto = texto.replace("\n", " ")

    texto = re.sub(r"\s+", " ", texto)

    return texto


COLUMNAS_OBLIGATORIAS = [
    "fecha",
    "especialidades médicas recibió atención",
    "inicio de su cita médica",
    "tiempo de espera",
    "comunicación",
    "trato recibido",
    "actitudes o comportamientos",
    "información brindada",
    "limpieza",
    "comodidad",
    "orden",
    "señalizacion",
    "nivel general de satisfacción",
    "comentario",
    "recomendaría",
    "ciudad",
    "sede"
]

def validar_columnas(df, columnas_obligatorias):

    columnas = [normalizar(c) for c in df.columns]

    faltantes = []

    for obligatoria in columnas_obligatorias:

        existe = any(
            obligatoria in columna
            for columna in columnas
        )

        if not existe:
            faltantes.append(obligatoria)

    return faltantes
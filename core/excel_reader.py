print("EXCEL READER CARGADO")

import pandas as pd


def limpiar_columna(columna):

    return (
        str(columna)
        .replace("\n", " ")
        .replace("\r", " ")
        .replace("\t", " ")
        .replace("  ", " ")
        .strip()
    )


def leer_excel(archivo):

    try:

        df = pd.read_excel(archivo)

        df = df.dropna(how="all")

        df.columns = [
            limpiar_columna(c)
            for c in df.columns
        ]

        return df

    except Exception as e:
        raise Exception(f"Error leyendo el archivo: {e}")
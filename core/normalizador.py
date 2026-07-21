import pandas as pd


def normalizar_texto(texto):

    if pd.isna(texto):
        return texto

    texto = str(texto).strip().upper()

    return texto


def normalizar_ciudad(df, columna):

    reemplazos = {

        "TULUA": "TULUA",
        "TULUÁ": "TULUA",
        "TULUA ": "TULUA",
        " TULUA": "TULUA",

        "BUGA": "Buga",
        "BUGA ": "Buga"

    }

    df[columna] = (
        df[columna]
        .astype(str)
        .str.strip()
        .str.upper()
        .replace(reemplazos)
    )

    return df


def normalizar_sede(df, columna):

    reemplazos = {

        "ALVERNIA": "Sede Alvernia",
        "SEDE ALVERNIA": "Sede Alvernia",
        "ALVERNIA ": "Sede Alvernia",

        "VICTORIA": "Sede Victoria",
        "SEDE VICTORIA": "Sede Victoria",
        "VICTORIA ": "Sede Victoria",

        "CESPEDES": "Sede Céspedes",
        "SEDE CESPEDES": "Sede Céspedes",
        "CÉSPEDES": "Sede Céspedes",
        "SEDE CÉSPEDES": "Sede Céspedes",
        "CESPEDES ": "Sede Céspedes"

    }

    df[columna] = (
        df[columna]
        .astype(str)
        .str.strip()
        .str.upper()
        .replace(reemplazos)
    )

    return df
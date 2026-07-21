import streamlit as st
import pandas as pd

from core.columnas import FECHA, SATISFACCION, RECOMENDACION
from core.kpis import calcular_satisfaccion, calcular_recomendacion


def mostrar_dashboard_general(archivos):

    dfs = []

    for nombre, df in archivos.items():

        if df is None:
            continue

        copia = df.copy()

        if FECHA in copia.columns:

            copia[FECHA] = pd.to_datetime(
                copia[FECHA],
                dayfirst=True,
                errors="coerce"
            )

        dfs.append(copia)

    if len(dfs) == 0:

        st.warning("No existen archivos cargados.")

        return

    df = pd.concat(
        dfs,
        ignore_index=True
    )

    st.header("📊 Indicadores Institucionales")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "📋 Total de Encuestas",
        len(df)
    )

    try:

        sat = calcular_satisfaccion(
            df,
            SATISFACCION
        )

    except:

        sat = 0

    c2.metric(
        "⭐ Satisfacción",
        f"{sat}%"
    )

    try:

        rec = calcular_recomendacion(
            df,
            RECOMENDACION
        )

    except:

        rec = 0

    c3.metric(
        "👍 Recomendación",
        f"{rec}%"
    )

    st.markdown("---")

    st.subheader("📈 Encuestas por mes")

    if FECHA in df.columns:

        meses = (
            df
            .dropna(subset=[FECHA])
            .groupby(df[FECHA].dt.to_period("M"))
            .size()
            .reset_index(name="Encuestas")
        )

        meses["Mes"] = meses[FECHA].astype(str)

        st.bar_chart(
            meses.set_index("Mes")["Encuestas"]
        )
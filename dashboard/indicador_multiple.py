import pandas as pd
import plotly.express as px
import streamlit as st


def mostrar_indicador_multiple(df, columna, titulo):

    with st.container(border=True):
    

        st.subheader(titulo)

        respuestas = (
            df[columna]
            .dropna()
            .astype(str)
    )

        total_encuestas = len(respuestas)

        opciones = []

        for respuesta in respuestas:

            opciones.extend([
                x.strip()
            for x in respuesta.split(",")
        ])

        tabla = (
            pd.Series(opciones)
            .value_counts()
            .reset_index()
    )

        tabla.columns = [
            "Comportamiento",
            "Cantidad"
    ]

        tabla["Porcentaje"] = round(
            tabla["Cantidad"] / total_encuestas * 100,
        1
    )

        st.metric(
            "Total de encuestas",
            total_encuestas
    )

        fig = px.bar(
            tabla,
            x="Cantidad",
            y="Comportamiento",
            orientation="h",
            text="Porcentaje"
    )

        fig.update_layout(
            height=450,
            yaxis=dict(categoryorder="total ascending")
    )

        st.plotly_chart(
            fig,
            use_container_width=True,
            key=f"grafico_{columna}"
    )

        st.dataframe(
            tabla,
            use_container_width=True,
            hide_index=True
    )
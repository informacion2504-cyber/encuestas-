import pandas as pd
import plotly.express as px
import streamlit as st


def mostrar_indicador(df, columna, titulo, respuestas_favorables):

    with st.container(border=True):

        # ---------------------------------
        # Preguntas de selección múltiple
        # ---------------------------------

        if len(respuestas_favorables) == 0:

            st.subheader(titulo)

            st.info(
                "Esta pregunta requiere un análisis especial por tratarse de una pregunta de selección múltiple."
            )

            return

        st.subheader(titulo)

        # ---------------------------------
        # Conteo de respuestas
        # ---------------------------------

        tabla = (
            df[columna]
            .fillna("Sin respuesta")
            .value_counts()
            .reset_index()
        )

        tabla.columns = [
            "Respuesta",
            "Cantidad"
        ]

        total = tabla["Cantidad"].sum()

        tabla["Porcentaje"] = (
            tabla["Cantidad"] / total * 100
        ).round(1)


        tabla["Acumulado"] = (
            tabla["Porcentaje"]
            .cumsum()
            .round(1)
        )

        # ---------------------------------
        # Normalizar respuestas
        # ---------------------------------

        tabla["Respuesta_Normalizada"] = (
            tabla["Respuesta"]
            .astype(str)
            .str.strip()
            .str.lower()
        )

        favorables_normalizadas = [
            r.strip().lower()
            for r in respuestas_favorables
        ]

        favorables = tabla[
            tabla["Respuesta_Normalizada"].isin(
                favorables_normalizadas
            )
        ]["Cantidad"].sum()

        tabla["Estado"] = tabla["Respuesta_Normalizada"].apply(
            lambda x: "✅ Favorable"
            if x in favorables_normalizadas
            else "❌ No favorable"
        )


        favorabilidad = round(
            favorables / total * 100,
            1
        )

        # ---------------------------------
        # Semáforo
        # ---------------------------------

        if favorabilidad >= 90:
            color = "🟢 Excelente"
        elif favorabilidad >= 80:
            color = "🟡 Aceptable"
        else:
            color = "🔴 Oportunidad de mejora"

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Favorabilidad",
            f"{favorabilidad}%"
        )

        c2.metric(
            "Total respuestas",
            total
        )

        c3.markdown(f"### {color}")

        # ---------------------------------
        # Gráfico
        # ---------------------------------

        fig = px.bar(
            tabla,
            x="Respuesta",
            y="Cantidad",
            text="Cantidad",
            color="Respuesta"
        )

        fig.update_layout(
            height=350,
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            key=f"grafico_{columna}"
        )

        # ---------------------------------
        # Tabla
        # ---------------------------------

        st.dataframe(
            tabla[
                [
                    "Respuesta",
                    "Cantidad",
                    "Porcentaje",
                    "Estado"
                ]
            ],
            use_container_width=True,
            hide_index=True
        )
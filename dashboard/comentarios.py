import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter

TEMAS = {

    "⏱️ Tiempo de espera": [
        "espera",
        "esperar",
        "demora",
        "demoró",
        "demoro",
        "retraso",
        "tarde",
        "rapido",
        "rápido"
    ],

    "👨‍⚕️ Atención médica": [
        "medico",
        "médico",
        "doctor",
        "profesional"
    ],

    "😊 Trato del personal": [
        "amable",
        "amabilidad",
        "trato",
        "cordial",
        "respeto",
        "educado",
        "atencion",
        "atención"
    ],

    "📢 Información": [
        "informacion",
        "información",
        "explico",
        "explicó",
        "orientacion",
        "orientación",
        "comunicacion",
        "comunicación"
    ],

    "🏥 Infraestructura": [
        "limpieza",
        "baño",
        "bano",
        "consultorio",
        "instalaciones",
        "silla",
        "comodidad",
        "señalizacion",
        "señalización"
    ]

}


# Palabras que no aportan significado
STOPWORDS = {
    "de", "la", "el", "los", "las", "y", "o", "que",
    "en", "un", "una", "es", "muy", "con", "del",
    "al", "por", "para", "se", "mi", "me", "su",
    "todo", "todos", "fue", "ha", "han", "como"
}


def mostrar_comentarios(df, columna):

    st.header("📝 Comentarios de los usuarios")

    comentarios = (
        df[columna]
        .dropna()
        .astype(str)
    )

    if len(comentarios) == 0:

        st.info("No existen comentarios para los filtros seleccionados.")
        return

    st.metric(
        "Comentarios recibidos",
        len(comentarios)
    )

    # -------------------------
    # Conteo de palabras
    # -------------------------

    palabras = []

    for comentario in comentarios:

        comentario = comentario.lower()

        comentario = comentario.replace(",", " ")
        comentario = comentario.replace(".", " ")
        comentario = comentario.replace(";", " ")
        comentario = comentario.replace(":", " ")

        for palabra in comentario.split():

            palabra = palabra.strip()

            if len(palabra) < 4:
                continue

            if palabra in STOPWORDS:
                continue

            palabras.append(palabra)

    conteo_temas = {}

    for tema, palabras_clave in TEMAS.items():

        cantidad = 0

        for comentario in comentarios:

            texto = comentario.lower()

            if any(
                palabra in texto
                for palabra in palabras_clave
            ):
                cantidad += 1

        conteo_temas[tema] = cantidad

    tabla = (
        pd.DataFrame(
            conteo_temas.items(),
            columns=[
                "Tema",
                "Frecuencia"
            ]
    )
        .sort_values(
            "Frecuencia",
            ascending=False
    )
)

    st.subheader("📈 Temas más mencionados")

    fig = px.bar(
        tabla,
        x="Frecuencia",
        y="Tema",
        orientation="h",
        text="Frecuencia"
    )

    fig.update_layout(
        height=450,
        yaxis=dict(categoryorder="total ascending")
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        key="grafico_comentarios"
    )

    st.dataframe(
        tabla,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("📄 Comentarios")

    with st.expander("Ver comentarios"):

        for comentario in comentarios:

            st.write("•", comentario)
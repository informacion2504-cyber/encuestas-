import streamlit as st

EXPERTICIA = [
    "experto",
    "expertos",
    "experiencia",
    "habil",
    "hábil",
    "conocimiento",
    "muy buena mano",
    "muy suaves",
    "no le dolió",
    "hacen muy bien su trabajo",
    "tiene experiencia"
]

TRATO_HUMANO = [
    "amable",
    "amables",
    "atento",
    "atentos",
    "cercanos",
    "respeto",
    "respetuosa",
    "respetuoso",
    "rápida",
    "todo bien",
    "muy bien",
    "bien",
    "excelente",
    "si",
    "sí",
    "claro que si"
]

OPORTUNIDADES = [
    "brusca",
    "confunden",
    "sangre",
    "no limpiaron",
    "no informaron",
    "demora",
    "mal",
    "chorrio",
    "no le informaron"
]


def mostrar_analisis_texto(df, columna, titulo):

    with st.container(border=True):

        st.subheader(titulo)

        if columna not in df.columns:
            st.error(f"No existe la columna:\n\n{columna}")
            return

        respuestas = (
            df[columna]
            .dropna()
            .astype(str)
        )

        experticia = []
        trato = []
        mejora = []
        otros = []

        for texto in respuestas:

            t = texto.lower()

            if any(x in t for x in OPORTUNIDADES):
                mejora.append(texto)

            elif any(x in t for x in EXPERTICIA):
                experticia.append(texto)

            elif any(x in t for x in TRATO_HUMANO):
                trato.append(texto)

            else:
                otros.append(texto)

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("🩺 Experticia", len(experticia))
        c2.metric("🤝 Trato humano", len(trato))
        c3.metric("⚠️ Oportunidades", len(mejora))
        c4.metric("📝 Otros", len(otros))

        st.markdown("---")

        if mejora:

            with st.expander(f"⚠️ Aspectos por mejorar ({len(mejora)})", expanded=True):

                for comentario in mejora[:10]:
                    st.write("•", comentario)

        if experticia:

            with st.expander(f"🩺 Comentarios sobre la experticia ({len(experticia)})"):

                for comentario in experticia[:10]:
                    st.write("•", comentario)

        if trato:

            with st.expander(f"🤝 Comentarios sobre el trato humano ({len(trato)})"):

                for comentario in trato[:10]:
                    st.write("•", comentario)

        if otros:

            with st.expander(f"📝 Otros comentarios ({len(otros)})"):

                for comentario in otros[:10]:
                    st.write("•", comentario)
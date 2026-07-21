import streamlit as st

from core.excel_reader import leer_excel


ENCUESTAS = [
    "Consulta Externa",
    "Hospitalización",
    "Cirugía",
    "Imágenes Diagnósticas",
    "Laboratorio",
    "Rehabilitación",
    "Urgencias"
]


def mostrar_carga_archivos():

    if "archivos" not in st.session_state:
        st.session_state["archivos"] = {}

    st.subheader("📂 Gestión de archivos")

    for encuesta in ENCUESTAS:

        col1, col2 = st.columns([3,2])

        with col1:

            if encuesta in st.session_state["archivos"]:

                df = st.session_state["archivos"][encuesta]

                st.success(f"✅ {encuesta} ({len(df)} registros)")

            else:

                st.error(f"❌ {encuesta}")

        with col2:

            archivo = st.file_uploader(
                "",
                type="xlsx",
                key=f"file_{encuesta}"
            )

            if archivo is not None:

                df = leer_excel(archivo)

                st.session_state["archivos"][encuesta] = df

def obtener_dataframe(encuesta):

    if encuesta in st.session_state["archivos"]:

        return st.session_state["archivos"][encuesta]

    return None

mostrar_carga_archivos()

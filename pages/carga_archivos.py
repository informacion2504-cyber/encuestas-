import streamlit as st
from pathlib import Path

from core.excel_reader import leer_excel

ARCHIVOS = {
    "Consulta Externa": "Consulta_Externa.xlsx",
    "Hospitalización": "Hospitalizacion.xlsx",
    "Cirugía": "Cirugia.xlsx",
    "Imágenes Diagnósticas": "Imagenes.xlsx",
    "Laboratorio": "Laboratorio.xlsx",
    "Rehabilitación": "Rehabilitacion.xlsx",
    "Urgencias": "Urgencias.xlsx",
}


def mostrar_carga_archivos():

    if "archivos" not in st.session_state:
        st.session_state["archivos"] = {}

    st.subheader("📂 Estado de las encuestas")

    for encuesta, archivo in ARCHIVOS.items():

        ruta = Path("datos") / archivo

        try:

            df = leer_excel(ruta)

            st.session_state["archivos"][encuesta] = df

            st.success(f"✅ {encuesta} ({len(df)} registros)")

        except Exception:

            st.error(f"❌ No se encontró {archivo}")


def obtener_dataframe(encuesta):

    return st.session_state["archivos"].get(encuesta)


mostrar_carga_archivos()


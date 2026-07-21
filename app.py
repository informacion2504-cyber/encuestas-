import streamlit as st
import plotly.express as px

from config import *

from core.excel_reader import leer_excel
from core.validator import validar_columnas
from core.columnas import *
from dashboard.indicador import mostrar_indicador
from dashboard.indicador_multiple import mostrar_indicador_multiple
from encuestas.configuracion import CONFIGURACION_ENCUESTAS
from core.encuestas.configuracion import CONFIG_COLUMNAS
from core.normalizador import normalizar_ciudad, normalizar_sede
from core.kpis import calcular_satisfaccion, calcular_recomendacion
import pandas as pd
from dashboard.comentarios import mostrar_comentarios
from pages.carga_archivos import obtener_dataframe
from dashboard.Analisis_texto import mostrar_analisis_texto
from dashboard.dashboard_general import mostrar_dashboard_general

st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout="wide"
)

# ==========================================
# MEMORIA DE ARCHIVOS
# ==========================================

if "archivos" not in st.session_state:
    st.session_state["archivos"] = {}

# ===================================================
# TITULO
# ===================================================

st.title("🏥 Dashboard de Satisfacción del Usuario")

st.markdown(
    "### Módulo de análisis de encuestas de satisfacción"
)

st.markdown("---")

# ===================================================
# CARGA DEL ARCHIVO
# ===================================================

opciones = ["📊 Todos los servicios"] + list(CONFIGURACION_ENCUESTAS.keys())

encuesta = st.selectbox(
    "Seleccione la encuesta",

    opciones
)

if encuesta == "📊 Todos los servicios":

    mostrar_dashboard_general(
        st.session_state["archivos"]
    )

    st.stop()


config = CONFIG_COLUMNAS[encuesta]

preguntas_encuesta = CONFIGURACION_ENCUESTAS[encuesta]["preguntas"]

# ===================================================
# LEER EXCEL
# ===================================================

try:

    df = obtener_dataframe(encuesta)

    if df is None:
        st.warning(
            f"Primero debe cargar el archivo de {encuesta} en la página 'Cargar archivos'.")
        st.stop()

    df = df.copy()

    st.write("REGISTROS AL CARGAR EL EXCEL:", len(df))

    st.success(f"📂 Usando archivo cargado previamente para {encuesta}")

     # =====================================
     # NORMALIZAR INFORMACIÓN
    # =====================================

    if config["usa_ciudad"]:
        df = normalizar_ciudad(
            df,
            CIUDAD
        )
    st.write("Después de normalizar ciudad:", len(df))
    # =====================================
    # FECHA, AÑO Y MES
    # =====================================

    df[FECHA] = pd.to_datetime(
        df[FECHA],
        dayfirst=True,
        errors="coerce"
)

    MESES = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
}

    df["Año"] = df[FECHA].dt.year

    df["Mes"] = (
        df[FECHA]
        .dt.month
        .map(MESES)
    )

    if config["usa_sede"]:
        df = normalizar_sede(
            df,
            SEDE
        )

    st.write("Después de normalizar sede:", len(df))
# Validación deshabilitada temporalmente mientras se configuran
# las demás encuestas.

    #if len(faltantes) > 0:

        #st.error("El archivo no corresponde a la encuesta.")

        #st.write("Faltan las siguientes columnas:")

        #for c in faltantes:
           # st.write("•", c)

        #st.stop()#

    st.success("Archivo cargado correctamente.")

    # ===================================================
    # FILTROS
    # ===================================================

    st.markdown("---")

    st.subheader("🔎 Filtros")

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:

        if config["usa_especialidad"] and ESPECIALIDAD in df.columns:

            especialidad = st.selectbox(
                "Especialidad",
                ["Todas"] + sorted(df[ESPECIALIDAD].dropna().unique())
        )

        else:

            especialidad = "Todas"

    with c2:

            if config["usa_ciudad"] and CIUDAD in df.columns:

                ciudad = st.selectbox(
                    "Ciudad",
                    ["Todas"] + sorted(df[CIUDAD].dropna().unique())
        )

            else:
                ciudad = "Todas"

    with c3:

        if config["usa_sede"] and SEDE in df.columns:

            sede = st.selectbox(
                "Sede",
                ["Todas"] + sorted(df[SEDE].dropna().unique())
        )

        else:
            sede = "Todas"

    with c4:
        
        año = st.selectbox(
            "Año",
            ["Todos"] + sorted(df["Año"].dropna().unique().tolist())
    )

    with c5:
        mes = st.selectbox(
            "Mes",
            ["Todos"] + list(MESES.values())
    )

    df_filtrado = df.copy()

    if config["usa_especialidad"] and ESPECIALIDAD in df.columns:

        if especialidad != "Todas":

            df_filtrado = df_filtrado[
                df_filtrado[ESPECIALIDAD] == especialidad
        ]

    if config["usa_ciudad"] and CIUDAD in df.columns:

        if ciudad != "Todas":

            df_filtrado = df_filtrado[
                df_filtrado[CIUDAD] == ciudad
        ]


    if  config["usa_sede"] and SEDE in df.columns:
        
        if sede != "Todas":
            df_filtrado = df_filtrado[
                df_filtrado[SEDE] == sede
        ]

    if año != "Todos":
        df_filtrado = df_filtrado[
            df_filtrado["Año"] == año
    ]

    if mes != "Todos":
        df_filtrado = df_filtrado[
            df_filtrado["Mes"] == mes
    ]

    st.write("Registros después de filtros:", len(df_filtrado))

    # ===================================================
    # KPIs GENERALES
    # ===================================================

    st.markdown("---")

    st.subheader("📊 Indicadores Generales")

    k1, k2, k3 = st.columns(3)

    # Total de encuestas
    k1.metric(
        "📋 Encuestas",
        len(df_filtrado)
    )

    k2.metric(
         "⭐ Satisfacción General",
         f"{calcular_satisfaccion(df_filtrado, SATISFACCION)}%"
)

    k3.metric(
        "👍 Recomendaría",
        f"{calcular_recomendacion(df_filtrado, RECOMENDACION)}%"
)

    
    # ==========================================
    # INDICADORES
    # ==========================================

    st.markdown("---")
    st.header("📊 Resultados de la Encuesta")


    if preguntas_encuesta is None:
        st.warning(
            "⚠️ Esta encuesta aún se encuentra en desarrollo."
    )

        st.stop()

    for categoria, preguntas in preguntas_encuesta.items():

        st.markdown("---")
        
        st.subheader(categoria)

        col1, col2 = st.columns(2)

        for i, pregunta in enumerate(preguntas):
            
            if i % 2 == 0:
                
                with col1:
                    
                    if pregunta["favorables"] == []:

                        mostrar_analisis_texto(
                            df=df_filtrado,
                            columna=pregunta["columna"],
                            titulo=pregunta["titulo"]
    )

                    elif pregunta["columna"] == MEDICO:

                        mostrar_indicador_multiple(
                            df=df_filtrado,
                            columna=pregunta["columna"],
                            titulo=pregunta["titulo"]
    )

                    else:

                        mostrar_indicador(
                            df=df_filtrado,
                            columna=pregunta["columna"],
                            titulo=pregunta["titulo"],
                            respuestas_favorables=pregunta["favorables"]
    )

            else:
            
                with col2:
                    
                    if pregunta["favorables"] == []:

                        mostrar_analisis_texto(
                            df=df_filtrado,
                            columna=pregunta["columna"],
                            titulo=pregunta["titulo"]
    )

                    elif pregunta["columna"] == MEDICO:

                        mostrar_indicador_multiple(
                            df=df_filtrado,
                            columna=pregunta["columna"],
                            titulo=pregunta["titulo"]
    )

                    else:

                        mostrar_indicador(
                        df=df_filtrado,
                        columna=pregunta["columna"],
                        titulo=pregunta["titulo"],
                        respuestas_favorables=pregunta["favorables"]
    )
                    

    st.markdown("---")

    mostrar_comentarios(
        df_filtrado,
        "¿Desea agregar algún comentario adicional sobre su experiencia o sugerencias para mejorar nuestro servicio?"
)     

    with st.expander("Ver datos"):

        st.dataframe(
            df_filtrado,
            use_container_width=True
        )

except Exception as e:

    import traceback

    st.error(e)

    st.code(traceback.format_exc())
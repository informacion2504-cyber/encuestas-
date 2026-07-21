from core.encuestas.cirugia import *
from core.columnas import SATISFACCION, RECOMENDACION

PREGUNTAS_CIRUGIA = {

    "😊 Experiencia durante la atención": [

        {
            "titulo": "Trato del equipo quirúrgico",
            "columna": TRATO_EQUIPO_QX,
            "favorables": [
                "Muy Satisfecho/a",
                "Satisfecho/a"
            ]
        },

        {
            "titulo": "Actitudes del personal médico",
            "columna": ACTITUDES_PERSONAL_MEDICO,
            "favorables": []
        }

    ],

    "⏱️ Oportunidad y comunicación": [

        {
            "titulo": "Tiempo para programación",
            "columna": TIEMPO_PROGRAMACION,
            "favorables": [
                "1 a 5 días calendario",
                "6 a 10 días calendario"
            ]
        },

        {
            "titulo": "Comunicación del procedimiento",
            "columna": COMUNICACION_PROCEDIMIENTO,
            "favorables": [
                "Sí",
                "Si"
            ]
        },
        
        {
            "titulo": "Información sobre medicamentos",
            "columna": INFORMACION_MEDICAMENTOS,
            "favorables": [
                "Totalmente clara",
                "Parcialmente clara"
            ]
        },

    ],


    "🏥 Infraestructura y comodidad": [

        {
            "titulo": "Limpieza",
            "columna": LIMPIEZA,
            "favorables": [
                "Excelente",
                "Aceptable"
            ]
        },

        {
            "titulo": "Comodidad",
            "columna": COMODIDAD,
            "favorables": [
                "Excelente",
                "Aceptable"
            ]
        },

        {
            "titulo": "Orden",
            "columna": ORDEN,
            "favorables": [
                "Excelente",
                "Aceptable"
            ]
        },

        {
            "titulo": "Señalización",
            "columna": SENALIZACION,
            "favorables": [
                "Excelente",
                "Aceptable"
            ]
        }

    ],

    "⭐ Resultado de la experiencia": [

        {
            "titulo": "Satisfacción General",
            "columna": SATISFACCION,
            "favorables": [
                "Muy satisfecho/a",
                "Satisfecho/a",
                "Neutral"
            ]
        },

        {
            "titulo": "Recomendación",
            "columna": RECOMENDACION,
            "favorables": [
                "Definitivamente sí",
                "Probablemente sí"
            ]
        }

    ]

}
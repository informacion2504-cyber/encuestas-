from core.encuestas.hospitalizacion import *
from core.columnas import SATISFACCION, RECOMENDACION

PREGUNTAS_HOSPITALIZACION = {

    "😊 Experiencia durante la atención": [

        {
            "titulo": "Trato del equipo de Hospitalización",
            "columna": TRATO_EQUIPO_HOSP,
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

    "⏱️ Oportunidad y seguimiento": [

        {
            "titulo": "Rondas del personal asistencial",
            "columna": RONDAS_OBSERVACION,
            "favorables": [
                "Una vez cada 1-2 horas"
            ]
        }

    ],

    "🏥 Infraestructura y comodidad": [

        {
            "titulo": "Infraestructura",
            "columna": INFRAESTRUCTURA,
            "favorables": [
                "Sí",
                "Si"
            ]
        },

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

    "🍽️ Alimentación": [

        {
            "titulo": "Información sobre la dieta",
            "columna": DIETA,
            "favorables": [
                "Sí",
                "Si"
            ]
        },

        {
            "titulo": "Calidad de la alimentación",
            "columna": COMIDA,
            "favorables": [
                "Muy satisfecho/a",
                "Satisfecho/a"
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
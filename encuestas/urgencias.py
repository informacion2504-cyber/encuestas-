from core.encuestas.urgencias import *

PREGUNTAS_URGENCIAS = {

    "😊 Experiencia en la atención": [

        {
            "titulo": "Orientación y comunicación",
            "columna": "¿Considera que la comunicación y el acompañamiento proporcionados por el personal de orientación fueron claros y efectivos?",
            "favorables": [
                "Excelente",
                "Bueno",
                "Aceptable"
            ]
        },

        {
            "titulo": "Personal administrativo",
            "columna": "¿Cómo calificaría el trato recibido por el personal administrativo de admisión y facturación de la institución?",
            "favorables": [
                "Excelente",
                "Bueno",
                "Aceptable"
            ]
        },

        {
            "titulo": "Personal médico",
            "columna": "¿Cómo calificaría el trato brindado por el personal médico que lo atendió ?",
            "favorables": [
                "Excelente",
                "Bueno",
                "Aceptable"
            ]
        },

        {
            "titulo": "Personal asistencial",
            "columna": "¿Experimentó un acompañamiento adecuado por parte de nuestro personal asistencial?",
            "favorables": [
                "Sí",
                "Si"
            ]
        },

        {
            "titulo": "Actitudes del personal médico",
            "columna": "¿Qué actitudes o comportamientos notó en el personal médico o especialista durante su atención? (Puede seleccionar una o más opciones)",
            "favorables": []
        },

        {
            "titulo": "Experticia del personal asistencial",
            "columna": "¿Considera que el personal asistencial (Enfermeros, Auxiliares de Enfermería) demostró experticia y habilidad en las actividades o procedimientos realizados durante su atención?",
            "favorables": []
        }

    ],

    "⏱️ Oportunidad y continuidad del servicio": [

        {
            "titulo": "Información brindada",
            "columna": "¿La información proporcionada por el personal que lo remitió, referente a procedimientos, medicamentos, citas o terapias, fue clara y exhaustiva?",
            "favorables": [
                "Totalmente clara",
                "Parcialmente clara"
            ]
        },

        {
            "titulo": "Llamada de seguimiento",
            "columna": "¿Recibió alguna llamada de seguimiento por parte del personal de Admisiones después de su atención en el servicio de urgencias, para el agendamiento de citas?",
            "favorables": [
                "Definitivamente sí",
                "Probablemente sí"
            ]
        },

        {
            "titulo": "Rondas médicas",
            "columna": "¿Con qué frecuencia diría usted que el personal médico o Especialista realizó rondas de observación y monitoreo ?",
            "favorables": [
                "Siempre",
                "Una vez cada 1-2 horas"
            ]
        },

        {
            "titulo": "Plan terapéutico",
            "columna": "Fue usted informado de manera clara y comprensible por el médico tratante sobre su plan terapéutico o tratamiento (incluyendo objetivos, pasos a seguir, posibles efectos y duración estimada)?",
            "favorables": [
                "Definitivamente sí",
                "Probablemente sí"
            ]
        },

        {
            "titulo": "Entrega de medicamentos",
            "columna": "¿Le fueron entregados los medicamentos prescritos o necesarios al finalizar su atención médica, y recibió información clara sobre su uso?",
            "favorables": [
                "Definitivamente sí",
                "Probablemente sí"
            ]
        }

    ],

    "🏥 Infraestructura y comodidad": [

        {
            "titulo": "Limpieza",
            "columna": "Evalúe la instalación donde recibió el servicio en los siguientes aspectos [Limpieza ]",
            "favorables": [
                "Excelente",
                "Aceptable"
            ]
        },

        {
            "titulo": "Comodidad",
            "columna": "Evalúe la instalación donde recibió el servicio en los siguientes aspectos [Comodidad ]",
            "favorables": [
                "Excelente",
                "Aceptable"
            ]
        },

        {
            "titulo": "Orden",
            "columna": "Evalúe la instalación donde recibió el servicio en los siguientes aspectos [Orden]",
            "favorables": [
                "Excelente",
                "Aceptable"
            ]
        },

        {
            "titulo": "Señalización",
            "columna": "Evalúe la instalación donde recibió el servicio en los siguientes aspectos [Señalizacion]",
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
from encuestas.consulta_externa import PREGUNTAS_CONSULTA_EXTERNA
from encuestas.rehabilitacion import PREGUNTAS_REHABILITACION
from encuestas.urgencias import PREGUNTAS_URGENCIAS
from encuestas.cirugia import PREGUNTAS_CIRUGIA
from encuestas.hospitalizacion import PREGUNTAS_HOSPITALIZACION
from core.columnas import*

CONFIGURACION_ENCUESTAS = {

    "Consulta Externa": {
        "preguntas": PREGUNTAS_CONSULTA_EXTERNA,
        "titulo": "Consulta Externa",
        "icono": "🩺",
    },

    "Hospitalización": {
        "preguntas": PREGUNTAS_HOSPITALIZACION,
        "titulo": "Hospitalización",
        "icono": "🛏️"
    },

    "Cirugía": {
        "preguntas": PREGUNTAS_CIRUGIA,
        "titulo": "Cirugía",
        "icono": "🏥",
        "satisfaccion": "Califique su nivel general de satisfacción con los servicios recibidos",
        "recomendacion": "¿Recomendaría la Clínica Dolormed S.A.S. a sus familiares o amigos para la prestación de servicios de salud?"
    },

    "Imágenes Diagnósticas": {
        "preguntas": None,
        "titulo": "Imágenes Diagnósticas",
        "icono": "🩻"
    },

    "Laboratorio": {
        "preguntas": None,
        "titulo": "Laboratorio",
        "icono": "🧪"
    },

    "Rehabilitación": {
        "preguntas": PREGUNTAS_REHABILITACION,
        "titulo": "Rehabilitación",
        "icono": "♿"
    },

    "Urgencias": {
        "preguntas": PREGUNTAS_URGENCIAS,
        "titulo": "Urgencias",
        "icono": "🚑"
    }

}
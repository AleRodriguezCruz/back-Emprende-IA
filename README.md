# back-Emprende-IA
Emprende IA: Design Doc del Backend

Link: (Link a este documento)

Author(s): Alejandra Rodriguez de la Cruz

Status: [Draft]

Última actualización: 2024-10-14
Contenido

    Objetivo

    Goals

    Non-Goals

    Background

    Overview

    Detailed Design

    Consideraciones

    Métricas

    Links

Objetivo

Construir un servicio de backend para Emprende IA. Este servicio recibirá una ubicación y, utilizando una lista de negocios existentes, identificará y devolverá las categorías de comercios con menor competencia en esa zona para ayudar a los emprendedores a tomar decisiones informadas.
Goals

    Procesar una consulta de texto (ej. "¿Qué negocios faltan en Maneadero?") para identificar una zona geográfica predefinida.

    Filtrar un conjunto de datos para aislar los negocios que se encuentran cerca del área de interés.

    Calcular y devolver una lista de categorías de negocios con baja saturación (oportunidades).

    Proveer los datos geolocalizados de los negocios existentes para que un frontend pueda visualizarlos en un mapa.

Non-Goals

    Ofrecer análisis predictivo sobre el éxito de un negocio.

    Soportar el registro de usuarios o el almacenamiento de búsquedas.

    Actualizar la base de datos de negocios en tiempo real desde fuentes externas.

    Soportar consultas de áreas geográficas no predefinidas en el sistema.

Background

Muchos emprendedores eligen su próximo negocio basándose en la intuición, lo que aumenta el riesgo de fracaso en mercados competidos. Emprende IA se creó para ofrecer una herramienta simple basada en datos que muestre la densidad comercial de una zona. La versión actual es un prototipo funcional hecho con Streamlit.
Overview

El sistema es una aplicación de Python que utiliza la librería Pandas para el análisis de datos. La lógica principal consiste en cargar un archivo CSV con datos de negocios, interpretar la solicitud del usuario para identificar una zona, aplicar un filtro geográfico, contar los negocios por categoría para encontrar las menos comunes y preparar los resultados.
Detailed Design
Solución 1: Prototipo Actual (Monolítico con Streamlit)

En esta fase, el frontend y el backend están fuertemente acoplados en una única aplicación.
Backend/Frontend

    Carga de datos: Una función carga el datos_ensenada.csv en un DataFrame de Pandas, usando el caché de Streamlit para optimizar.

    Procesamiento de Lenguaje: Se realiza una búsqueda simple de subcadenas (ej. "Maneadero") en la consulta del usuario.

    Filtro Geográfico: Se utiliza una aproximación de "cuadro delimitador" (bounding box) para filtrar los negocios en un área rectangular alrededor de un punto central.

    Lógica de Negocio: Se usa value_counts() y nsmallest(5) de Pandas para encontrar las 5 categorías con menor frecuencia.

Solución 2: Backend Desacoplado con API REST

Esta es la evolución planificada, separando la lógica en un servicio independiente para mayor flexibilidad y escalabilidad.
Frontend

    Será cualquier cliente (aplicación web, móvil, etc.) capaz de consumir una API REST. No es parte del alcance de este backend.

Backend (Flask y Pandas)

    Framework: Se usará Flask para construir los endpoints de la API.

    Manejo de Datos: El servidor Flask cargará el archivo CSV en un DataFrame de Pandas al iniciar. Este DataFrame se mantendrá en memoria para atender todas las solicitudes, eliminando la necesidad de una base de datos externa.

    Endpoint Principal: Se definirá una ruta como GET /api/v1/oportunidades que aceptará parámetros de consulta como ?zona=maneadero.

    Respuesta (JSON): El servicio devolverá una respuesta estructurada en formato JSON para que el frontend la pueda interpretar fácilmente.

    {
      "zona_analizada": "Maneadero",
      "oportunidades": [
        "Ferretería",
        "Papelería",
        "Gimnasio"
      ],
      "negocios_existentes": [
        {"nombre": "Tacos El Fénix", "categoria": "Restaurante", "lat": 31.715, "lon": -116.568},
        {"nombre": "Abarrotes Mary", "categoria": "Tienda de abarrotes", "lat": 31.716, "lon": -116.565}
      ]
    }

Consideraciones

    Simpleza: El enfoque con Flask y Pandas permite centrarse en los fundamentos de la creación de APIs sin la complejidad de una base de datos.

    Precisión Geográfica: Se mantendrá el método del "cuadro delimitador", que es suficiente para el alcance del proyecto.

    Calidad de los Datos: La utilidad de las recomendaciones depende directamente de la calidad del archivo CSV.

    Escalabilidad: Cargar el CSV en memoria es práctico para el conjunto de datos actual, pero no sería viable para un conjunto de datos a nivel nacional.

Métricas

    Tiempo de respuesta: Medir el tiempo en milisegundos que tarda la API en procesar y devolver una respuesta.

    Tasa de éxito de consulta: Porcentaje de solicitudes que identifican una zona correctamente y devuelven un análisis válido.

Links

    Repositorio del Proyecto

    Documentación de Pandas

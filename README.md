# Emprende IA - Backend

Link:https://github.com/AleRodriguezCruz/back-Emprende-IA.git
Author(s): Alejandra Rodríguez de la Cruz  
Status: Draft  
Última actualización: 2024-10-14

---

## Contenido

- [Objetivo](#objetivo)  
- [Goals](#goals)  
- [Non-Goals](#non-goals)  
- [Background](#background)  
- [Overview](#overview)  
- [Detailed Design](#detailed-design)  
- [Consideraciones](#consideraciones)  
- [Métricas](#métricas)  
- [Links](#links)  
- [Licencia](#licencia)  

---

## Objetivo

Construir un servicio backend para Emprende IA que reciba una ubicación y, usando la lista de negocios del archivo db-ens-bc.csv, identifique y devuelva las categorías de comercios con menor competencia en esa zona. Esta información ayudará a emprendedores a tomar decisiones basadas en datos.

---

## Goals

- Identificar zonas geográficas desde consultas de texto.  
- Filtrar negocios existentes en la zona indicada.  
- Encontrar las categorías de negocio con menor saturación.  
- Entregar datos que permitan mostrar esas oportunidades en un mapa.  

---

## Non-Goals

- No análisis predictivo de éxito comercial.  
- No manejo de usuarios ni almacenamiento de búsquedas.  
- No actualización automática del dataset.  
- Solo funciona con zonas definidas.  

---

## Background

Muchos emprenden sin suficientes datos, lo que puede ser riesgoso. Este proyecto aporta información sencilla basada en datos para elegir oportunidades con menos competencia.

---

## Overview

Aplicación en Python con Pandas y Flask que carga un CSV con datos de negocios, procesa consultas y devuelve oportunidades y negocios geolocalizados vía API REST.

---

## Detailed Design

### Solución 1: Prototipo Streamlit

Backend y frontend juntos para demostración rápida, procesamiento de texto, filtro geográfico y resultados simples.

### Solución 2: API REST con Flask

Backend desacoplado que mantiene datos en memoria y ofrece endpoint para consultas estructuradas y respuesta JSON clara.

---

## Consideraciones

- Simplicidad y mantenimiento son prioridad.  
- Filtro geográfico en bounding box suficiente para el alcance.  
- Dependencia de la calidad y actualización del CSV.  
- No preparado para datos masivos sin optimización.  

---

## Métricas

- Tiempo de respuesta medido en milisegundos.  
- Porcentaje de consultas con zona identificada y respuesta válida.  

---
## Cómo Usar la API (Endpoints)

La API sigue los principios REST y utiliza el prefijo base `/excel/negocio`.

---

### 1. Obtener todos los negocios
Devuelve una lista con todos los negocios del archivo CSV.

* **Método:** `GET`
* **Ruta:** `/excel/negocio/`
* **Respuesta Exitosa (200 OK):**
    ```json
    [
      {
        "id": 0,
        "categoria_negocio": "ABULONES CULTIVADOS",
        "latitud": 31.8621572,
        "longitud": -116.6267073
      },
      {
        "id": 1,
        "categoria_negocio": "AGRICOLA DOS MARES",
        "latitud": 31.06657818,
        "longitud": -116.2098943
      }
    ]
    ```

---

### 2. Obtener un negocio por su ID
Busca y devuelve un negocio específico usando su ID (el número de fila del archivo).

* **Método:** `GET`
* **Ruta:** `/excel/negocio/{negocio_id}`
* **Parámetros:**
    * `negocio_id` (entero): El ID del negocio que deseas obtener.
* **Respuesta Exitosa (200 OK):**
    ```json
    {
      "id": 0,
      "categoria_negocio": "ABULONES CULTIVADOS",
      "latitud": 31.8621572,
      "longitud": -116.6267073
    }
    ```
* **Respuesta de Error (404 Not Found):**
    ```json
    {
      "detail": "Negocio con ID '9999' no encontrado."
    }
    ```

---

### 3. Crear, Actualizar y Eliminar (Simulados)
Los siguientes endpoints están implementados pero funcionan como una simulación, ya que no modifican permanentemente el archivo en un entorno como Vercel.

* **Crear un Negocio:**
    * **Método:** `POST`
    * **Ruta:** `/excel/negocio/`
* **Actualizar un Negocio:**
    * **Método:** `PUT`
    * **Ruta:** `/excel/negocio/{negocio_id}`
* **Eliminar un Negocio:**
    * **Método:** `DELETE`
    * **Ruta:** `/excel/negocio/{negocio_id}`
## Links

- Repositorio del proyecto:   https://github.com/AleRodriguezCruz/back-Emprende-IA.git
- Pandas Docs: https://pandas.pydata.org/docs/  
- Flask Docs: https://flask.palletsprojects.com/en/latest/  

---


import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# =====================================================================
# CONFIGURACIÓN INICIAL
# =====================================================================

# --- Nombres de las columnas REALES de tu archivo datos_ensenada.csv ---
COLUMNA_CATEGORIA = 'categoria_negocio'
COLUMNA_LATITUD = 'latitud'
COLUMNA_LONGITUD = 'longitud'
# ---------------------------------------------------------------------

# Crear la aplicación FastAPI
app = FastAPI(
    title="Emprende IA API v2",
    description="API que funciona con el archivo datos_ensenada.csv y lista para Vercel.",
    version="2.0.0",
)

# --- Modelo de Datos (ajustado a tu CSV) ---
# Como no tenemos todos los campos, lo simplificamos.
class Negocio(BaseModel):
    id: int  # Usaremos el número de fila como ID
    categoria_negocio: str
    latitud: float
    longitud: float

# --- Carga de datos ---
df = None
try:
    df = pd.read_csv("datos_ensenada.csv", encoding='latin1')
    
    # --- CREACIÓN DE UN ID ÚNICO ---
    # Como tu archivo no tiene un ID, creamos uno usando el índice (0, 1, 2, ...).
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'id'}, inplace=True)
    
    print("✅ Archivo CSV cargado y con IDs generados exitosamente.")

except Exception as e:
    print(f"❌ Error al cargar o procesar el CSV: {e}")
    df = pd.DataFrame()

# =====================================================================
# ENDPOINTS DE LA API (Funcionales con tu CSV)
# =====================================================================


PREFIX = "/excel/negocio"

@app.get("/")
def read_root():
    return {"mensaje": "API funcionando. Visita /docs para probar los endpoints."}

# --- GET: Obtener TODOS los negocios ---
@app.get(f"{PREFIX}/", tags=["Negocios"])
def get_all_negocios():
    if df.empty:
        raise HTTPException(status_code=500, detail="Los datos no se pudieron cargar.")
    return df.to_dict(orient='records')

# --- GET: Obtener UN negocio por su ID (el número de fila) ---
@app.get(f"{PREFIX}/{{negocio_id}}", tags=["Negocios"])
def get_negocio_por_id(negocio_id: int):
    if df.empty:
        raise HTTPException(status_code=500, detail="Los datos no se pudieron cargar.")
    
    # Buscamos el negocio por el ID que generamos
    negocio = df[df['id'] == negocio_id]
    
    if negocio.empty:
        raise HTTPException(status_code=404, detail=f"Negocio con ID '{negocio_id}' no encontrado.")
    
    return negocio.to_dict(orient='records')[0]

# --- PUT: Actualizar un negocio (simulado) ---
# Nota: Los cambios no se guardarán permanentemente en Vercel.
@app.put(f"{PREFIX}/{{negocio_id}}", tags=["Negocios"])
def actualizar_negocio(negocio_id: int, negocio_actualizado: Negocio):
    if df.empty:
        raise HTTPException(status_code=500, detail="Los datos no se pudieron cargar.")
        
    if negocio_id not in df['id'].values:
        raise HTTPException(status_code=404, detail=f"Negocio con ID '{negocio_id}' no encontrado para actualizar.")
    
    # Lógica para actualizar el DataFrame (simulado)
    # df.loc[df['id'] == negocio_id, [COLUMNA_CATEGORIA, COLUMNA_LATITUD, COLUMNA_LONGITUD]] = [negocio_actualizado.categoria_negocio, negocio_actualizado.latitud, negocio_actualizado.longitud]
    
    return {"mensaje": f"Negocio {negocio_id} actualizado (simulación).", "data": negocio_actualizado.dict()}

# --- POST y DELETE (Simulados) ---
# Los dejamos como simulación porque modificar el archivo en Vercel es complejo y temporal.
@app.post(f"{PREFIX}/", status_code=201, tags=["Negocios"])
def crear_negocio(negocio: Negocio):
    return {"mensaje": "Negocio recibido (simulación, no se guardará).", "data": negocio.dict()}

@app.delete(f"{PREFIX}/{{negocio_id}}", tags=["Negocios"])
def eliminar_negocio(negocio_id: int):
    if df.empty or negocio_id not in df['id'].values:
        raise HTTPException(status_code=404, detail=f"Negocio con ID '{negocio_id}' no encontrado.")
    return {"mensaje": f"Negocio {negocio_id} eliminado (simulación)."}

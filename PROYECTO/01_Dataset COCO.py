# Importamos la librería para cargar datasets
from datasets import load_dataset

# Cargamos la versión oficial del dataset COCO 2017, split train
dataset = load_dataset("coco", "2017", split="train")

# Clases para filtrar cajas, maletas, etc
clases_caja = ['box', 'suitcase', 'handbag']

# Usaremos un conjunto para evitar repeticiones
cajas_detectadas = set()

# Recorremos los primeros 2000 ejemplos (puedes cambiar este número)
for ejemplo in dataset.select(range(2000)):
    # Extraemos las categorías etiquetadas para cada objeto
    categorias = ejemplo['objects']['label']
    
    # Buscamos clases que contengan alguna palabra relacionada a cajas
    for clase_id in categorias:
        # El label en COCO está en número, necesitamos mapa de ID a nombre
        # Pero este dataset NO trae directamente el mapeo en la carga, por lo que lo definimos:
        # Mapeo oficial COCO (simplificado para cajas)
        mapa_id_nombre = {
            24: 'backpack',
            25: 'umbrella',
            26: 'handbag',  # bolsa de mano
            27: 'tie',
            28: 'suitcase', # maleta
            # No hay "box" explícito, a veces se usa suitcase o handbag
        }
        
        nombre_clase = mapa_id_nombre.get(clase_id, None)
        
        # Si la clase está en las categorías de cajas, la agregamos
        if nombre_clase in clases_caja:
            cajas_detectadas.add(nombre_clase)

# Mostramos las clases detectadas
print("Modelos de caja detectados en el dataset COCO 2017:")
for clase in sorted(cajas_detectadas):
    print(f"- {clase}")


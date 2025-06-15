import tensorflow as tf
from tensorflow.keras.models import load_model

# Ruta al archivo .h5 (debes asegurarte de que el archivo esté en esa ubicación)
ruta_modelo = 'mnist-fashion-model.h5'

try:
    # Cargar el modelo
    modelo = load_model(ruta_modelo)

    # Mostrar resumen del modelo cargado
    print("Modelo cargado exitosamente:")
    modelo.summary()

except Exception as e:
    print("Error al cargar el modelo:")
    print(e)

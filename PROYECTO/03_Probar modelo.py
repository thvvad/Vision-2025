import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.datasets import fashion_mnist

# Carga el modelo preentrenado que está en la misma carpeta
model = load_model('mnist-fashion-model.h5')

# Carga el dataset Fashion MNIST para pruebas
(_, _), (x_test, y_test) = fashion_mnist.load_data()
x_test = x_test / 255.0  # Normaliza los datos

# Cambia la forma para que sea compatible con el modelo (batch, alto, ancho, canales)
x_test = np.expand_dims(x_test, axis=-1)

# Realiza predicciones sobre las primeras 5 imágenes
predictions = model.predict(x_test[:5])

# Muestra las predicciones y las etiquetas reales
for i, pred in enumerate(predictions):
    clase_predicha = np.argmax(pred)
    clase_real = y_test[i]
    print(f"Imagen {i+1}: Clase predicha = {clase_predicha}, Clase real = {clase_real}")

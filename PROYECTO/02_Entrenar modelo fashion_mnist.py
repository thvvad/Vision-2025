import tensorflow as tf
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
x_test = x_test / 255.0  # Normalizar

# Descargar modelo preentrenado desde Keras (reconstrucción básica)
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Cargar pesos preentrenados entrenados con Fashion MNIST (tendrás que entrenarlo una sola vez)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Si ya entrenaste una vez y guardaste el modelo, puedes hacer:
# model = load_model('modelo_fashion_mnist.h5')

# Entrenar (una sola vez)
model.fit(x_train, y_train, epochs=5)

# Guardar para usar después sin volver a entrenar
model.save('modelo_fashion_mnist.h5')

# Evaluar
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Precisión en test: {test_acc:.2f}')

# Probar predicción
predicciones = model.predict(x_test)

# Mostrar imagen con etiqueta predicha
plt.imshow(x_test[0], cmap='gray')
plt.title(f'Etiqueta predicha: {np.argmax(predicciones[0])}')
plt.show()

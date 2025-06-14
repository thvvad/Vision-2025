# Importamos las librerías necesarias
from datasets import load_dataset
import matplotlib.pyplot as plt

# Cargamos el dataset desde Hugging Face
dataset = load_dataset("fashion_mnist")

# Mostramos el número de imágenes en cada subconjunto
print(f"Número de imágenes en entrenamiento: {len(dataset['train'])}")
print(f"Número de imágenes en prueba: {len(dataset['test'])}")

# Mostramos las llaves (columnas) del dataset
print("Columnas disponibles:", dataset["train"].column_names)

# Definimos las etiquetas en texto (el dataset usa números del 0 al 9)
labels = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

# Mostramos 10 imágenes aleatorias del set de entrenamiento
def mostrar_ejemplos(dataset, split="train", num_ejemplos=10):
    plt.figure(figsize=(12, 4))
    for i in range(num_ejemplos):
        ejemplo = dataset[split][i]
        imagen = ejemplo["image"]
        etiqueta = ejemplo["label"]
        
        plt.subplot(1, num_ejemplos, i + 1)
        plt.imshow(imagen, cmap="gray")
        plt.title(labels[etiqueta])
        plt.axis("off")
    plt.suptitle(f"Primeros {num_ejemplos} ejemplos de '{split}'")
    plt.show()

# Llamamos a la función para visualizar
mostrar_ejemplos(dataset)

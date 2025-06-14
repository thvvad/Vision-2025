from datasets import load_dataset
import matplotlib.pyplot as plt

# Cargar dataset fashion_mnist (train y test)
dataset_train = load_dataset("fashion_mnist", split="train")
dataset_test = load_dataset("fashion_mnist", split="test")

# Etiquetas (clases) en fashion_mnist
label_names = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

# Mostrar 5 imágenes con sus etiquetas
for i in range(5):
    image = dataset_train[i]["image"]
    label = dataset_train[i]["label"]

    plt.imshow(image, cmap="gray")
    plt.title(f"Etiqueta: {label_names[label]} ({label})")
    plt.axis("off")
    plt.show()

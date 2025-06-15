# Importa la función load_dataset del módulo datasets (de Hugging Face), para cargar el dataset Fashion MNIST
from datasets import load_dataset

# Importa matplotlib.pyplot para graficar imágenes
import matplotlib.pyplot as plt

# Carga el dataset "fashion_mnist" desde Hugging Face
dataset = load_dataset("fashion_mnist")

# Diccionario que asigna un nombre legible a cada etiqueta numérica
etiquetas = {
    0: "T-shirt/top",   # Etiqueta 0 representa camisetas
    1: "Trouser",        # Pantalones
    2: "Pullover",       # Suéteres
    3: "Dress",          # Vestidos
    4: "Coat",           # Abrigos
    5: "Sandal",         # Sandalias
    6: "Shirt",          # Camisas
    7: "Sneaker",        # Tenis
    8: "Bag",            # Bolsas
    9: "Ankle boot"      # Botas
}

# Cantidad de imágenes por clase que se mostrarán en cada fila
imagenes_por_clase = 5

# Crea una figura de 10 filas (una por clase) y 5 columnas (una por imagen)
plt.figure(figsize=(imagenes_por_clase * 2, 20))  # Ancho y alto del lienzo

# Bucle para cada clase de prenda (etiquetas del 0 al 9)
for clase in range(10):
    # Contador de cuántas imágenes se han mostrado para esta clase
    count = 0

    # Recorre todas las imágenes del conjunto de entrenamiento
    for i, (img, label) in enumerate(zip(dataset['train']['image'], dataset['train']['label'])):
        # Si la etiqueta actual coincide con la clase buscada
        if label == clase:
            # Calcula el número de subplot (posición en la figura)
            index = clase * imagenes_por_clase + count + 1

            # Crea el subplot correspondiente en la figura
            plt.subplot(10, imagenes_por_clase, index)

            # Muestra la imagen en escala de grises
            plt.imshow(img, cmap='gray')

            # Muestra el nombre de la clase solo en la primera imagen de esa fila
            if count == 0:
                plt.ylabel(etiquetas[clase], fontsize=12)

            # Oculta los ejes de la imagen
            plt.axis('off')

            # Aumenta el contador de imágenes mostradas para esta clase
            count += 1

            # Si ya se mostraron suficientes imágenes de esta clase, se sale del bucle interno
            if count >= imagenes_por_clase:
                break

# Ajusta el espaciado para que no se encimen las imágenes ni los textos
plt.tight_layout()

# Muestra todas las imágenes organizadas por tipo de prenda
plt.show()

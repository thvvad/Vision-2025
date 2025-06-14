# Importa la función load_dataset del módulo datasets (de Hugging Face), para cargar el dataset Fashion MNIST
from datasets import load_dataset

# Importa matplotlib.pyplot para crear gráficos e imágenes
import matplotlib.pyplot as plt

# Carga el dataset "fashion_mnist" desde Hugging Face y lo guarda en la variable 'dataset'
dataset = load_dataset("fashion_mnist")

# Crea un diccionario que traduce los números de clase a nombres legibles de prendas
etiquetas = {
    0: "T-shirt/top",   # Etiqueta 0 representa camisetas o blusas
    1: "Trouser",        # Etiqueta 1 representa pantalones
    2: "Pullover",       # Etiqueta 2 representa suéteres
    3: "Dress",          # Etiqueta 3 representa vestidos
    4: "Coat",           # Etiqueta 4 representa abrigos
    5: "Sandal",         # Etiqueta 5 representa sandalias
    6: "Shirt",          # Etiqueta 6 representa camisas
    7: "Sneaker",        # Etiqueta 7 representa tenis
    8: "Bag",            # Etiqueta 8 representa bolsas
    9: "Ankle boot"      # Etiqueta 9 representa botas
}

# Extrae las primeras 9 imágenes del conjunto de entrenamiento y las guarda en la lista 'imagenes'
imagenes = dataset['train']['image'][:9]

# Extrae las primeras 9 etiquetas (números) correspondientes a las imágenes anteriores
labels = dataset['train']['label'][:9]

# Crea una figura de 9x9 pulgadas para mostrar las imágenes en una cuadrícula
plt.figure(figsize=(9, 9))

# Bucle para mostrar las 9 imágenes y sus etiquetas
for i in range(9):
    # Crea una subfigura en la posición i+1 de una cuadrícula de 3 filas por 3 columnas
    plt.subplot(3, 3, i+1)

    # Muestra la imagen en escala de grises
    plt.imshow(imagenes[i], cmap='gray')

    # Asigna como título el nombre de la prenda correspondiente a la etiqueta de esa imagen
    plt.title(etiquetas[labels[i]])

    # Oculta los ejes de la imagen para que se vea limpia
    plt.axis('off')

# Ajusta automáticamente el espaciado para que no se sobrepongan las imágenes ni títulos
plt.tight_layout()

# Muestra en pantalla la figura con las 9 imágenes
plt.show()

from datasets import load_dataset  # Cargar datasets de Hugging Face
import matplotlib.pyplot as plt     # Para mostrar imágenes
import matplotlib.patches as patches
from PIL import Image
import requests
from io import BytesIO

# Cargar el dataset (split = 'train' para entrenamiento)
dataset = load_dataset("ashraq/face-mask-detection", split="train")

# Mostrar una imagen con su caja de rostro
ejemplo = dataset[0]
url = ejemplo['image']
box = ejemplo['bbox']  # bounding box [x, y, ancho, alto]

# Descargar la imagen
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# Dibujar la imagen con la caja
fig, ax = plt.subplots(1)
ax.imshow(img)

# Dibujar rectángulo (bounding box)
rect = patches.Rectangle((box[0], box[1]), box[2], box[3], linewidth=2, edgecolor='r', facecolor='none')
ax.add_patch(rect)
plt.title(f"Etiqueta: {ejemplo['label']}")
plt.show()

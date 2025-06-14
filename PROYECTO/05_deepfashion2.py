from datasets import load_dataset
import matplotlib.pyplot as plt

# Carga el dataset deepfashion2
dataset = load_dataset("andrewjones/deepfashion2")

# Revisa las splits disponibles
print("Splits disponibles:", dataset.keys())

# Mira la estructura de un ejemplo
print("Ejemplo de datos en train:")
print(dataset['train'][0])

# Mostrar una imagen y sus anotaciones (bounding boxes)
def mostrar_imagen_y_bboxes(data):
    image = data['image']
    plt.imshow(image)
    ax = plt.gca()
    for bbox in data['labels']['boxes']:
        x1, y1, x2, y2 = bbox
        width = x2 - x1
        height = y2 - y1
        rect = plt.Rectangle((x1, y1), width, height, edgecolor='red', facecolor='none', linewidth=2)
        ax.add_patch(rect)
    plt.title("Imagen con bounding boxes")
    plt.axis('off')
    plt.show()

# Muestra la primera imagen del split train
mostrar_imagen_y_bboxes(dataset['train'][0])

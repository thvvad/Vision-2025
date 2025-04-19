# Practica 3: Histograma de una imagen

# Importar librerías necesarias
import cv2  # OpenCV para procesamiento de imágenes
import matplotlib.pyplot as plt  # Matplotlib para mostrar imágenes y graficar

# Cargar imagen a color
img1 = cv2.imread('tata.jpg')  # Cambia 'tata.jpg' por la ruta de tu imagen

# Convertir a escala de grises
img2 = cv2.imread('tata.jpg', cv2.IMREAD_GRAYSCALE)

# Convertir imagen BGR a RGB (para que se vea bien en matplotlib)
img1_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

# Calcular el histograma de la imagen en escala de grises
hist = cv2.calcHist([img2], [0], None, [256], [0, 256])

# Crear una figura para mostrar las imágenes y el histograma
plt.figure(figsize=(12, 5))  # Ancho x Alto en pulgadas

# Mostrar imagen original (a color, convertida a RGB)
plt.subplot(1, 3, 1)  # 1 fila, 3 columnas, posición 1
plt.imshow(img1_rgb)
plt.title('Imagen original (color)')
plt.axis('off')  # Oculta los ejes

# Mostrar imagen en escala de grises
plt.subplot(1, 3, 2)  # Posición 2
plt.imshow(img2, cmap='gray')
plt.title('Escala de grises')
plt.axis('off')

# Mostrar histograma de la imagen en escala de grises
plt.subplot(1, 3, 3)  # Posición 3
plt.plot(hist, color='black')
plt.title('Histograma (grises)')
plt.xlabel('Valor de intensidad')
plt.ylabel('Número de píxeles')
plt.grid(True)

# Ajustar el diseño para que no se encimen los elementos
plt.tight_layout()

# Mostrar todo
plt.show()


# Esperar a que el usuario presione una tecla
cv2.waitKey(0)

# Cerrar todas las ventanas abiertas de OpenCV
cv2.destroyAllWindows()


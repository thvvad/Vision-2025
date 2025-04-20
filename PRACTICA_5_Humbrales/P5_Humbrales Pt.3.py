import numpy as np
import matplotlib.pyplot as plt
import cv2

# Cargar la imagen (asegúrate de tener una imagen de una página de un libro)
img = cv2.imread('bookpage.jpg')  # Reemplaza con el path de tu imagen
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convertir a escala de grises

# Definir el valor máximo para los píxeles umbralizados
max_val = 255

# Variar los parámetros para observar los efectos

# Primer caso:
thresh1 = cv2.adaptiveThreshold(
    gray, max_val, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Segundo caso: 
thresh2 = cv2.adaptiveThreshold(
    gray, max_val, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 55, 2)

# Tercer caso: 
thresh3 = cv2.adaptiveThreshold(
    gray, max_val, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Cuarto caso:
thresh4 = cv2.adaptiveThreshold(
    gray, max_val, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 55, 2)

# Mostrar los resultados en distintas ventanas para comparar los efectos
plt.figure(figsize=(12, 12))

# Primer umbral adaptativo
plt.subplot(2, 2, 1)
plt.imshow(thresh1, cmap='gray')
plt.title("Caso 1: BLOQUE=11, C=2")
plt.axis('off')

# Segundo umbral adaptativo
plt.subplot(2, 2, 2)
plt.imshow(thresh2, cmap='gray')
plt.title("Caso 2: BLOQUE=55, C=2")
plt.axis('off')

# Tercer umbral adaptativo (gaussiano)
plt.subplot(2, 2, 3)
plt.imshow(thresh3, cmap='gray')
plt.title("Caso 3: GAUSSIANO, BLOQUE=11, C=2")
plt.axis('off')

# Cuarto umbral adaptativo (gaussiano)
plt.subplot(2, 2, 4)
plt.imshow(thresh4, cmap='gray')
plt.title("Caso 4: GAUSSIANO, BLOQUE=55, C=2")
plt.axis('off')

# Mostrar todas las imágenes
plt.tight_layout()
plt.show()

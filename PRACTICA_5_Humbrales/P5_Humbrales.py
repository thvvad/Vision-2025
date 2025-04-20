#Practica 5: Humbrales

import numpy as np
import matplotlib.pyplot as plt
import cv2

# Carga la imagen en color (formato BGR)
img = cv2.imread('bookpage.jpg')

# Aplica umbralización binaria directamente sobre la imagen en color
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

# Convierte a escala de grises
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Umbral fijo sobre la imagen en escala de grises
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

# Umbral adaptativo Gaussiano
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                             cv2.THRESH_BINARY, 115, 1)

# Umbral de Otsu
retval3, otsu = cv2.threshold(grayscaled, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Prepara figura con subplots
plt.figure(figsize=(10, 8))

# Mostrar imagen original (convertida de BGR a RGB)
plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original')
plt.axis('off')

# Mostrar threshold aplicado sobre imagen a color
plt.subplot(2, 3, 2)
plt.imshow(cv2.cvtColor(threshold, cv2.COLOR_BGR2RGB))
plt.title('Threshold (color)')
plt.axis('off')

# Mostrar threshold aplicado sobre imagen en grises
plt.subplot(2, 3, 3)
plt.imshow(threshold2, cmap='gray')
plt.title('Threshold (gray)')
plt.axis('off')

# Mostrar umbral adaptativo gaussiano
plt.subplot(2, 3, 4)
plt.imshow(gaus, cmap='gray')
plt.title('Adaptativo Gaussiano')
plt.axis('off')

# Mostrar umbral de Otsu
plt.subplot(2, 3, 5)
plt.imshow(otsu, cmap='gray')
plt.title('Otsu')
plt.axis('off')

# Muestra todas las imágenes
plt.tight_layout()
plt.show()

# Practica 3: Histograma de una imagen

# Importar librerias
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('v2.jpeg')    # Cargar imagen
img2 = cv2.imread('v2.jpeg', cv2.IMREAD_GRAYSCALE)    # Convertir a escala de grises

cv2.imshow('Imagen 1',img1)             # Mostrar la imagen
cv2.imshow('Imagen 2',img2)             # Mostrar la imagen
hist = cv2.calcHist([img2], [0], None, [256], [0,256])
plt.plot(hist)
plt.show()

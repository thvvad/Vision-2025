# Practica 2: Operaciones Aritmeticas... Traslacion de una imagen
# Vanessa Aguirre Diaz

# Importar librerias:
import cv2
import numpy as np

# Cargar imagen
img = cv2.imread('tata.jpg')

# Dimensiones originales
alto, ancho = img.shape[:2]

# Definir traslación (mueve la imagen 150 píxeles a la derecha y 100 abajo)
Tx, Ty = 150, 100

# Crear matriz de traslación
M = np.float32([[1, 0, Tx], [0, 1, Ty]])

# Ajustar el tamaño del lienzo
nuevo_ancho = ancho + Tx
nuevo_alto = alto + Ty

# Aplicar traslación con nuevo tamaño
img_trasladada = cv2.warpAffine(img, M, (nuevo_ancho, nuevo_alto))

# Mostrar imágenes
cv2.imshow('Imagen Original', img)
cv2.imshow('Imagen Trasladada (Lienzo Ajustado)', img_trasladada)

cv2.waitKey(0)
cv2.destroyAllWindows()

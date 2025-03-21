# Practica 2: Operaciones Aritmeticas... Rotar una imagen
# Vanessa Aguirre Diaz

# Importar librerias:
import cv2
import numpy as np

# Cargar imagen
img = cv2.imread('chimmy.jpg')

# Obtener dimensiones
(h, w) = img.shape[:2]

# Definir el centro de la imagen
centro = (w // 2, h // 2)

# Definir ángulo de rotación
angulo = 45

# Calcular la matriz de rotación
M = cv2.getRotationMatrix2D(centro, angulo, 1.0)

# Calcular nuevas dimensiones (evitar que se recorte)
cos = np.abs(M[0, 0])
sin = np.abs(M[0, 1])

nuevo_ancho = int((h * sin) + (w * cos))
nuevo_alto = int((h * cos) + (w * sin))

# Ajustar la matriz de transformación para centrar la imagen
M[0, 2] += (nuevo_ancho / 2) - centro[0]
M[1, 2] += (nuevo_alto / 2) - centro[1]

# Aplicar la transformación
img_rotada = cv2.warpAffine(img, M, (nuevo_ancho, nuevo_alto))

# Mostrar imágenes
cv2.imshow('Original', img)
cv2.imshow('Rotada sin cortar', img_rotada)

cv2.waitKey(0)                  # Esperar a que el usuario presione una tecla para cerrar la ventana
cv2.destroyAllWindows()         # Cerrar todas las ventanas de OpenCV.

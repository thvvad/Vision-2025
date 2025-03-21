# Practica 2: Operaciones Aritmeticas... Rotar una imagen
# Vanessa Aguirre Diaz

# Importar librerias:
import cv2
import numpy as np

# Cargar imagen
img = cv2.imread('chimmy.jpg')

# Rotar 90° antihorario con NumPy
img_rotada_90 = np.transpose(img, (1, 0, 2))[:, ::-1]   # Solo funciona para 90°

# Mostrar imágenes
cv2.imshow('Original', img)
cv2.imshow('Rotada 90°', img_rotada_90)

cv2.waitKey(0)                  # Esperar a que el usuario presione una tecla para cerrar la ventana
cv2.destroyAllWindows()         # Cerrar todas las ventanas de OpenCV.

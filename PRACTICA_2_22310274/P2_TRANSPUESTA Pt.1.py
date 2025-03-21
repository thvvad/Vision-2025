# Practica 2: Operaciones Aritmeticas... Transpuesta
# Vanessa Aguirre Diaz

# Importar librerias:
import cv2
import numpy as np

img = cv2.imread('tata.jpg')  # Cargar imagen

img_trans1 = cv2.transpose(img)    # Aplicar transposición
img_trans2 = np.transpose(img, (1, 0, 2))  # Intercambia alto y ancho

# Mostrar resultados
cv2.imshow('Imagen Original', img)
cv2.imshow('Imagen Transpuesta con cv2.transpose', img_trans1)
cv2.imshow('Imagen Transpuesta con np.transpose', img_trans2)

cv2.waitKey(0)                  # Esperar a que el usuario presione una tecla para cerrar la ventana
cv2.destroyAllWindows()         # Cerrar todas las ventanas de OpenCV.

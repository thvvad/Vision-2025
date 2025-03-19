# Practica 2: Operaciones Aritmeticas
# Vanessa Aguirre Diaz

# Importar librerias:
import cv2
import numpy as np

# 500 x 250
img1 = cv2.imread('3D-Matplotlib.png')  # Cargar imagen 1
img2 = cv2.imread('mainsvmimage.png')   # Cargar imagen 2

add = img1+img2                 # Sumar ambas imagenes pixel por pixel
                                # Si la suma supera los 255 habrá un desbordamiento
cv2.imshow('Suma',add)          # Mostrar la imagen que resulta de la suma
cv2.waitKey(0)                  # Esperar a que el usuario presione una tecla para cerrar la ventana
cv2.destroyAllWindows()         # Cerrar todas las ventanas de OpenCV.

# Practica 1 Pt.1: Cargar una imagen en escala de grises
# Por Vanessa Aguirre Diaz

import cv2                                          # Importa la biblioteca OpenCV, que se usa para procesamiento de imágenes y visión artificial.
import numpy as np                                  # Importa NumPy, que es útil para manejar matrices y operaciones matemáticas.
from matplotlib import pyplot as plt                # Importa pyplot de Matplotlib, aunque en este código no se usa.

img = cv2.imread('perro.jpg',cv2.IMREAD_GRAYSCALE)  # Carga la imagen llamada perro.jpg en modo escala de grises (cv2.IMREAD_GRAYSCALE equivale a 0).
cv2.imshow('image',img)                             # Muestra la imagen en una ventana con el título image.
cv2.waitKey(0)                                      # Espera a que el usuario presione una tecla para cerrar la ventana.
cv2.destroyAllWindows()                             # Cierra todas las ventanas de OpenCV abiertas.

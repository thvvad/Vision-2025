# Practica 1 Pt.2: Cargar una imagen en escala de grises y dibujar varias lineas de color azul
# Por Vanessa Aguirre Diaz

# Importamos las bibliotecas necesarias:
import cv2                              # OpenCV para procesamiento de imágenes
import numpy as np                      # NumPy (no se usa en este código, pero está importado)
from matplotlib import pyplot as plt    # Matplotlib para visualizar la imagen

img = cv2.imread('perro.jpg', cv2.IMREAD_GRAYSCALE)     # Cargamos la imagen 'perro.jpg' en escala de grises

# Mostramos la imagen con Matplotlib
plt.imshow(img, cmap='gray', interpolation='bicubic')   # cmap='gray' la muestra en escala de grises
                                                        # Usa interpolación bicubic para mejorar la visualización.

plt.xticks([]), plt.yticks([])# Ocultamos los valores de los ejes X e Y para una visualización más limpia

# Dibujamos una línea en color azul ('b') con un grosor de 5 píxeles
plt.plot([200, 200, 400, 600, 600, 500, 400, 300, 200], [100, 300, 500, 300, 100, 50, 150, 50, 100], 'b', linewidth=5)    #x,y
# La línea pasa por los puntos (200,100), (300,200) y (400,300)

plt.show() # Mostramos la imagen con la línea dibujada encima

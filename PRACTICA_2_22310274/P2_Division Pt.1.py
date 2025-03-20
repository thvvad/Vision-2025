# Practica 2: Operaciones Aritmeticas... Multiplicacion
# Vanessa Aguirre Diaz

# Importar librerias:
import cv2
import numpy as np

# 440 x 500
img1 = cv2.imread('tata.jpg')       # Cargar imagen 1
img2 = cv2.imread('chimmy.jpg')     # Cargar imagen 2

# Multiplicar ambas imagenes pixel por pixel
#Pt.1:
division = img1 / (img2 + 1e-5)     # Se añade epsilon para evitar división por 0
                                    # Realiza la división, pero si un píxel en img2 es 0, generará valores muy altos
#Pt.2:
div_cv2 = cv2.divide(img1,img2)     # Evita divisiones por 0 automáticamente.

cv2.imshow('Imagen 1',img1)         # Mostrar la imagen 1
cv2.imshow('Imagen 2',img2)         # Mostrar la imagen 2
cv2.imshow('Division directa',division)                         # Mostrar la imagen que resulta de la division directa con signo
cv2.imshow('Division con la funcion cv2.divide',div_cv2)        # Mostrar la imagen que resulta de la division con la funcion cv2.divide

cv2.waitKey(0)                  # Esperar a que el usuario presione una tecla para cerrar la ventana
cv2.destroyAllWindows()         # Cerrar todas las ventanas de OpenCV.

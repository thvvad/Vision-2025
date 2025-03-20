# Practica 2: Operaciones Aritmeticas... Negacion
# Vanessa Aguirre Diaz

# Importar librerias:
import cv2
import numpy as np

# 440 x 500
img1 = cv2.imread('tata.jpg')    # Cargar imagen
img2 = cv2.imread('tata.jpg', cv2.IMREAD_GRAYSCALE)    # Misma imagen a escala de grises

#Pt.1:
img1_neg = 255- img1                # Operacion directa
img2_neg = 255- img2                # Operacion directa

#Pt.2:
neg1_cv2 = cv2.bitwise_not(img1)
neg2_cv2 = cv2.bitwise_not(img2) 

cv2.imshow('Imagen 1',img1)             # Mostrar la imagen
cv2.imshow('Imagen 2',img2)             # Mostrar la imagen
cv2.imshow('Negacion directa 1',img1_neg)                         # Mostrar la imagen que resulta de la negacion directa
cv2.imshow('Negacion directa 2',img2_neg)                         # Mostrar la imagen que resulta de la negacion directa 
cv2.imshow('Negacion 1 con la funcion cv2.bitwise',neg1_cv2)      # Mostrar la imagen que resulta de la negacion con la funcion cv2.bitwise
cv2.imshow('Negacion 2 con la funcion cv2.bitwise',neg2_cv2)      # Mostrar la imagen que resulta de la negacion con la funcion cv2.bitwise

cv2.waitKey(0)                  # Esperar a que el usuario presione una tecla para cerrar la ventana
cv2.destroyAllWindows()         # Cerrar todas las ventanas de OpenCV.

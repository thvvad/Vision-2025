# Practica 2: Operaciones Aritmeticas... Resta
# Vanessa Aguirre Diaz

# Importar librerias:
import cv2
import numpy as np

# 440 x 500
img1 = cv2.imread('tata.jpg')       # Cargar imagen 1
img2 = cv2.imread('chimmy.jpg')     # Cargar imagen 2

# Sumar ambas imagenes pixel por pixel
#Pt.1:
add = img1-img2                 # Si la resta supera los 0 habrá un desbordamiento negativo
#Pt.2:
add_cv2 = cv2.subtract(img1,img2)    # Si la resta es menor a 0, el valor se limita a 0 (no hay desbordamiento negativo).
#Pt.3: 
weighted = cv2.addWeighted(img1, 0.7, img2, -0.3, 0)     # Cada imagen tendrá un peso diferente

cv2.imshow('Imagen 1',img1)         # Mostrar la imagen 1
cv2.imshow('Imagen 2',img2)         # Mostrar la imagen 2
cv2.imshow('Resta directa',add)                     # Mostrar la imagen que resulta de la suma directa con signo
cv2.imshow('Resta sin desbordamiento',add_cv2)      # Mostrar la imagen que resulta de la resta con la funcion cv2.subtract
cv2.imshow('weighted',weighted)                     # Mostrar la imagen con diferentes pesos

cv2.waitKey(0)                                      # Esperar a que el usuario presione una tecla para cerrar la ventana
cv2.destroyAllWindows()                             # Cerrar todas las ventanas de OpenCV.

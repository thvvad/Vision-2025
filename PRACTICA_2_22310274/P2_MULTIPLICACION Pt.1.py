# Practica 2: Operaciones Aritmeticas... Multiplicacion
# Vanessa Aguirre Diaz

# Importar librerias:
import cv2
import numpy as np

# 500 x 250
img1 = cv2.imread('3D-Matplotlib.png')  # Cargar imagen 1
img2 = cv2.imread('mainsvmimage.png')   # Cargar imagen 2

# Multiplicar ambas imagenes pixel por pixel
#Pt.1:
multiplicacion = img1*img2              # Si la multiplicacion supera los 255 habrá un desbordamiento
#Pt.2:
mult_cv2 = cv2.multiply(img1,img2)      # Si la multiplicacion excede 255, el valor se limita a 255 (no hay desbordamiento).
                                        # Ideal para aplicar máscaras o efectos de fusión

cv2.imshow('Imagen 1',img1)                                         # Mostrar la imagen 1
cv2.imshow('Imagen 2',img2)                                         # Mostrar la imagen 2
cv2.imshow('Multiplicacion directa',multiplicacion)                 # Mostrar la imagen que resulta de la multiplicacion directa con signo
cv2.imshow('Multiplicacion con la funcion cv2.multiply',mult_cv2)   # Mostrar la imagen que resulta de la multiplicacion con la funcion cv2.multiply

cv2.waitKey(0)                  # Esperar a que el usuario presione una tecla para cerrar la ventana
cv2.destroyAllWindows()         # Cerrar todas las ventanas de OpenCV.

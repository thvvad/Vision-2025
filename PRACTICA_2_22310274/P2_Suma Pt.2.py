# Practica 2 Pt.4: Superponer una nueva imagen y que esta tenga prioridad sobre la primera
# Vanessa Aguirre Diaz

import cv2
import numpy as np

# Cargar dos imagenes
img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainlogo.png')

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape     # Se obtienen las dimensiones (alto, ancho, canales de color) del logo (img2)
roi = img1[0:rows, 0:cols ]         # Se extrae la región de interés (roi) de la imagen base (img1), del mismo tamaño que img2

# Now create a mask of logo and create its inverse mask
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)        # Convierte img2 (el logo) a escala de grises

# add a threshold
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)    # Convierte la imagen en una máscara binaria negativa (invierte los valores)

mask_inv = cv2.bitwise_not(mask)    #Invierte los valores de la máscara (mask):
                                        # El logo pasa a ser negro (0).
                                        # El fondo pasa a ser blanco (255).

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)  # Quitar la parte del logo en la región de interés

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)    # Extraer solo la parte del logo (sin fondo)

dst = cv2.add(img1_bg,img2_fg)  # Se suma img1_bg (fondo sin logo) con img2_fg (solo el logo)
img1[0:rows, 0:cols ] = dst     # Se inserta esta nueva imagen en la región de interés (img1[0:rows, 0:cols])

cv2.imshow('Imagen con el logo',img1)       # Mostrar la imagen final con el logo colocado
cv2.waitKey(0)                              # Esperar a que se presione una tecla
cv2.destroyAllWindows()                     # Cerrar todas las ventanas

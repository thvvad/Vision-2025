# Practica 4:Extraer una ROI (Region de interes) circular

#Importar libreria
import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('v.jpeg')

if imagen is None:
    print("Error: No se pudo cargar la imagen.")
    exit()

# Centro del círculo y radio
centro_x = 200
centro_y = 150
radio = 100

# Dibujar el círculo sobre la imagen original
cv2.circle(imagen, (centro_x, centro_y), radio, (0, 255, 0), 2)

# Crear una máscara del mismo tamaño que la imagen, inicialmente negra (cero)
mascara = np.zeros(imagen.shape[:2], dtype=np.uint8)

# Dibujar un círculo blanco en la máscara en la posición deseada
cv2.circle(mascara, (centro_x, centro_y), radio, 255, -1)

# Aplicar la máscara sobre la imagen para extraer solo la región circular
roi_circular = cv2.bitwise_and(imagen, imagen, mask=mascara)

# Mostrar la imagen original con el círculo dibujado
cv2.imshow("Imagen con ROI circular", imagen)

# Mostrar solo la ROI circular (el resto está negro)
cv2.imshow("ROI Circular", roi_circular)

cv2.waitKey(0)
cv2.destroyAllWindows()

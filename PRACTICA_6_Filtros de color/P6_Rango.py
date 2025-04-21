# Rango de colores que abarca el filtro

import cv2
import numpy as np

# Define los valores HSV mínimo y máximo
min_HSV = np.array([0, 150, 150])   # Puedes cambiar estos valores
max_HSV = np.array([0, 255, 255])  # Recuerda que H en OpenCV va de 0 a 179

# Crea una imagen de 256x300 píxeles (tamaño ajustable)
height, width = 100, 300
img = np.zeros((height, width, 3), dtype=np.uint8)

# Recorre cada píxel horizontalmente y asigna un color entre min_HSV y max_HSV
for x in range(width):
    ratio = x / (width - 1)
    hsv_color = min_HSV + (max_HSV - min_HSV) * ratio
    hsv_color = np.uint8([[hsv_color]])  # Necesita ser en formato (1,1,3) para convertir
    bgr_color = cv2.cvtColor(hsv_color, cv2.COLOR_HSV2BGR)[0][0]
    img[:, x] = bgr_color  # Pinta toda la columna con ese color

# Muestra el resultado en una ventana
cv2.imshow('Rango de colores HSV', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

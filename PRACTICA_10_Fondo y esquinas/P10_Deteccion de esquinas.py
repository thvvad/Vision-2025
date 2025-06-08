# Practica 10: Detección de esquinas
# Hacerlo sobre el filtro de color mejorado para quitar el fondo
# Pt 1: resultados de este codigo
# Pt 2: adaptar este codigo al filtro

# Importa la librería NumPy, que permite trabajar con matrices y operaciones matemáticas
import numpy as np

# Importa OpenCV, que se usa para procesamiento de imágenes y visión por computadora
import cv2

# Lee una imagen desde un archivo y la guarda en la variable 'img'
img = cv2.imread('opencv-corner-detection-sample.jpg')

# Convierte la imagen a escala de grises (necesario para aplicar detección de esquinas)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convierte la imagen en escala de grises a tipo de dato float32, requerido por la función de esquinas
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.1, 10) # Aplica el algoritmo de detección de esquinas Shi-Tomasi
#  - gray: imagen en escala de grises
#  - 100: número máximo de esquinas a detectar
#  - 0.01: calidad mínima aceptada de la esquina (entre 0 y 1)
#  - 10: distancia mínima entre esquinas detectadas


# Convierte las coordenadas de las esquinas a enteros (para poder usarlas en funciones de dibujo)
corners = np.int0(corners)

# Recorre cada esquina detectada
for corner in corners:
    # Extrae las coordenadas x e y de cada esquina (ravel aplana el array)
    x, y = corner.ravel()
    # Dibuja un círculo en la imagen original sobre cada esquina detectada
    # Parámetros:
    #  - img: imagen sobre la que se dibuja
    #  - (x, y): centro del círculo
    #  - 3: radio del círculo
    #  - 255: color (blanco en escala de grises)
    #  - -1: indica que el círculo se rellena completamente
    cv2.circle(img, (x, y), 3, 255, -1)

# Muestra la imagen con las esquinas detectadas en una ventana llamada 'Corner'
cv2.imshow('Corner', img)



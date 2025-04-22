#Practica 6: Filtro de color RGB (rojo)

import cv2                     # Importa la librería OpenCV para visión por computadora
import numpy as np             # Importa NumPy para trabajar con arreglos numéricos

# Inicia la captura de video desde la cámara (0 es la cámara principal)
cap = cv2.VideoCapture(0)

# Define el rango mínimo y máximo del color rojo en RGB
# Rango mas abierto
min_RGB = np.array([150, 0, 0])       # R: alto, G: bajo, B: bajo (rojo)
max_RGB = np.array([255, 150, 150])   # Hasta rojo más claro, sin llegar a rosado

# Rango mas cerrado
#min_RGB = np.array([150, 0, 0])       # R: alto, G: bajo, B: bajo (rojo)
#max_RGB = np.array([255, 100, 100])   # Hasta rojo más claro, sin llegar a rosado

# OpenCV usa formato BGR en lugar de RGB, por lo que invertimos el orden
bgr_min = min_RGB[::-1]           # Invierte los valores a BGR (Blue, Green, Red)
bgr_max = max_RGB[::-1]

# Crear una imagen que muestre el degradado del rango BGR detectado
def create_color_bar(min_color, max_color, width=300, height=50):
    # Crea una barra horizontal con un gradiente entre los colores min y max
    bar = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(width):
        alpha = i / width
        color = (1 - alpha) * min_color + alpha * max_color
        bar[:, i] = color
    return bar

# Crear la barra de color visualmente del rango
color_bar = create_color_bar(bgr_min, bgr_max)

# ---------- Bucle principal para video en vivo ------------------------------------------------
while True:
    ret, frame = cap.read()           # Lee un frame de la cámara
    if not ret:                       # Si no se pudo leer, rompe el bucle
        break

    # Crea una máscara con los píxeles dentro del rango BGR definido (color rojo)
    mask = cv2.inRange(frame, bgr_min, bgr_max)

    # Aplica la máscara al frame original: muestra solo los píxeles que estén dentro del rango
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Muestra la imagen original
    cv2.imshow('frame', frame)

    # Muestra la máscara en blanco y negro (blanco = rojo detectado)
    cv2.imshow('mask', mask)

    # Muestra la imagen resultante con solo los tonos rojos visibles
    cv2.imshow('res', res)

    # Mostrar la barra del rango de color detectado
    cv2.imshow('Color Range (RGB)', color_bar)

    # Espera 5 ms por una tecla; si se presiona ESC (código 27), se rompe el bucle
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Libera la cámara
cap.release()

# Cierra todas las ventanas abiertas
cv2.destroyAllWindows()

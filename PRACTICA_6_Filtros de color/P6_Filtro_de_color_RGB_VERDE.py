# Practica 6: Filtro de color RGB (verde)

import cv2                     # Importa la librería OpenCV para visión por computadora
import numpy as np             # Importa NumPy para trabajar con arreglos numéricos

# Inicia la captura de video desde la cámara (0 es la cámara principal)
cap = cv2.VideoCapture(0)

# Define el rango mínimo y máximo del color verde en RGB
min_RGB = np.array([0, 150, 0])        # G: medio-alto, R y B bajos
max_RGB = np.array([150, 255, 150])    # Verde claro, permite mezcla con un poco de azul o rojo

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

# ---------- Bucle principal para video en vivo --------------------------
while True:
    ret, frame = cap.read()           # Lee un frame de la cámara
    if not ret:                       # Si no se pudo leer, rompe el bucle
        break

    # Crea una máscara con los píxeles dentro del rango BGR definido (color verde)
    mask = cv2.inRange(frame, bgr_min, bgr_max)

    # Aplica la máscara al frame original: muestra solo los píxeles que estén dentro del rango
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Muestra la imagen original
    cv2.imshow('frame', frame)

    # Muestra la máscara en blanco y negro (blanco = verde detectado)
    cv2.imshow('mask', mask)

    # Muestra la imagen resultante con solo los tonos verdes visibles
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

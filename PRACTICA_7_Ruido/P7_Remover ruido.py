# Practica 7: Tomar una captura

import cv2                     # Importa la librería OpenCV para visión por computadora
import numpy as np             # Importa NumPy para trabajar con arreglos numéricos

# Inicia la captura de video desde la cámara (0 es la cámara principal)
cap = cv2.VideoCapture(0)

# Define el rango mínimo y máximo del color azul en RGB
min_RGB = np.array([0, 0, 150])        # B: alto, G: bajo, R: bajo (azul)
max_RGB = np.array([150, 150, 255])    # Azul claro sin llegar a celeste brillante   

# OpenCV usa formato BGR en lugar de RGB, por lo que invertimos el orden
bgr_min = min_RGB[::-1]           # Invierte los valores a BGR (Blue, Green, Red)
bgr_max = max_RGB[::-1]

# Crear una imagen que muestre el degradado del rango BGR detectado
def create_color_bar(min_color, max_color, width=300, height=50):
    bar = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(width):
        alpha = i / width
        color = (1 - alpha) * min_color + alpha * max_color
        bar[:, i] = color
    return bar

# Crear la barra de color visualmente del rango
color_bar = create_color_bar(bgr_min, bgr_max)

# Variables para almacenar los frames capturados al presionar espacio
frame_original = None
frame_mask = None
frame_res = None
frame_bar = None

# ---------- Bucle principal para video en vivo --------------------------
while True:
    ret, frame = cap.read()           # Lee un frame de la cámara
    if not ret:
        break

    # Crea una máscara con los píxeles dentro del rango BGR definido (color azul)
    mask = cv2.inRange(frame, bgr_min, bgr_max)

    # Aplica la máscara al frame original
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Muestra las ventanas
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('Color Range (RGB)', color_bar)

    # Espera 5 ms por una tecla
    key = cv2.waitKey(5) & 0xFF

    if key == 27:  # ESC
        break
    elif key == 32:  # Espacio
        frame_original = frame.copy_


# Cierra todas las ventanas abiertas
cv2.destroyAllWindows()

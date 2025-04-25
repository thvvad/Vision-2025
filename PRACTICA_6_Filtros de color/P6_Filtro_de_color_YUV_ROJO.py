# Practica 6: Filtro de color YUV (rojo)

import cv2
import numpy as np

# Inicia la captura de video desde la cámara principal
cap = cv2.VideoCapture(0)

# Define el rango mínimo y máximo del color rojo en YUV
# El canal V (rojo) debe ser alto para detectar tonos rojos
min_YUV = np.array([0, 120, 140])     # Y bajo, U medio, V alto
max_YUV = np.array([255, 180, 255])   # Y alto, U medio, V máximo

# Crear una barra de gradiente visual basada en el rango YUV
def create_color_bar_yuv(min_color, max_color, width=300, height=50):
    bar = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(width):
        alpha = i / width
        yuv_color = (1 - alpha) * min_color + alpha * max_color
        yuv_color = np.clip(yuv_color, 0, 255).astype(np.uint8)
        bgr_color = cv2.cvtColor(np.uint8([[yuv_color]]), cv2.COLOR_YUV2BGR)[0][0]
        bar[:, i] = bgr_color
    return bar

# Crear la barra de color
color_bar = create_color_bar_yuv(min_YUV, max_YUV)

# ---------- Bucle principal para video en vivo --------------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir el frame de BGR a YUV
    yuv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)

    # Crear una máscara con los píxeles dentro del rango YUV definido (color rojo)
    mask = cv2.inRange(yuv_frame, min_YUV, max_YUV)

    # Aplicar la máscara al frame original
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Mostrar la imagen original
    cv2.imshow('frame', frame)

    # Mostrar la máscara en blanco y negro
    cv2.imshow('mask', mask)

    # Mostrar la imagen

# Practica 6: Filtro de color YUV (verde)

import cv2                     # Importa la librería OpenCV para visión por computadora
import numpy as np             # Importa NumPy para trabajar con arreglos numéricos

# Inicia la captura de video desde la cámara (0 es la cámara principal)
cap = cv2.VideoCapture(0)

# Define el rango mínimo y máximo del color verde en YUV
# Estos valores pueden ajustarse según el tono de verde que se quiera detectar
min_YUV = np.array([0, 0, 0])         # Límite inferior (Y, U, V)
max_YUV = np.array([255, 130, 100])   # Límite superior

# Crear una imagen que muestre el degradado del rango YUV detectado (no muy representativo, pero se mantiene visual)
def create_color_bar_yuv(min_color, max_color, width=300, height=50):
    bar = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(width):
        alpha = i / width
        yuv_color = (1 - alpha) * min_color + alpha * max_color
        bgr_color = cv2.cvtColor(np.uint8([[yuv_color]]), cv2.COLOR_YUV2BGR)[0][0]
        bar[:, i] = bgr_color
    return bar

color_bar = create_color_bar_yuv(min_YUV, max_YUV)

# ---------- Bucle principal para video en vivo --------------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir el frame de BGR a YUV
    yuv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)

    # Crear máscara con los píxeles dentro del rango YUV definido
    mask = cv2.inRange(yuv_frame, min_YUV, max_YUV)

    # Aplicar la máscara al frame original
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Mostrar la imagen original
    cv2.imshow('frame', frame)

    # Mostrar la máscara en blanco y negro
    cv2.imshow('mask', mask)

    # Mostrar la imagen resultante con los tonos verdes detectados
    cv2.imshow('res', res)

    # Mostrar la barra de color
    cv2.imshow('Color Range (YUV)', color_bar)

    # Salir si se presiona ESC
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

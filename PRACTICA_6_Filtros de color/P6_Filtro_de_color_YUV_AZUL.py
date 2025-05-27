# Practica 6: Filtro de color YUV (AZUL)

import cv2          # Para procesamiento de imágenes y visión por computadora
import numpy as np  # Para trabajar con arreglos y operaciones numéricas

# Inicia captura de video desde la cámara web
cap = cv2.VideoCapture(0)

# Define los valores YUV mínimo y máximo para detectar azul
# El canal U es el que representa los tonos azulados
min_YUV = np.array([0, 150, 90])      # Y bajo, U alto (azul), V medio
max_YUV = np.array([200, 255, 130])    # Y alto, U máximo, V bajo

# ---------- Visualización del rango de colores YUV ----------
height, width = 100, 300
img = np.zeros((height, width, 3), dtype=np.uint8)

for x in range(width):
    ratio = x / (width - 1)
    yuv_color = min_YUV + (max_YUV - min_YUV) * ratio
    yuv_color = np.clip(yuv_color, 0, 255).astype(np.uint8)
    bgr_color = cv2.cvtColor(np.uint8([[yuv_color]]), cv2.COLOR_YUV2BGR)[0][0]
    img[:, x] = bgr_color

# Muestra la barra de colores solo una vez al inicio
cv2.imshow('Rango de colores YUV', img)

# ---------- Bucle principal para video en vivo ----------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convierte el frame a YUV
    yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)

    # Crea una máscara con los valores del color azul en YUV
    mask = cv2.inRange(yuv, min_YUV, max_YUV)

    # Aplica la máscara al frame original
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Muestra las ventanas
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    # Presiona ESC para salir
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Libera recursos
cap.release()
cv2.destroyAllWindows()

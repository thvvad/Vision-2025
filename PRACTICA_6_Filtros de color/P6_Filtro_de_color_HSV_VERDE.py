# Practica 6: Filtros de color HSV (VERDE)

import cv2          # Para procesamiento de imágenes y visión por computadora
import numpy as np  # Para trabajar con arreglos y operaciones numéricas

# Inicia captura de video desde la cámara web (índice 0)
cap = cv2.VideoCapture(0)

# Define los valores HSV mínimo y máximo
# Rango mas abierto:
#min_HSV = np.array([35, 50, 50])     
#max_HSV = np.array([85, 255, 255])

# Mas cerrado
min_HSV = np.array([50, 100, 100])     
max_HSV = np.array([70, 255, 255])

# ---------- Visualización del rango de colores ----------
height, width = 100, 300
img = np.zeros((height, width, 3), dtype=np.uint8)

for x in range(width):
    ratio = x / (width - 1)
    hsv_color = min_HSV + (max_HSV - min_HSV) * ratio
    hsv_color = np.uint8([[hsv_color]])
    bgr_color = cv2.cvtColor(hsv_color, cv2.COLOR_HSV2BGR)[0][0]
    img[:, x] = bgr_color

# Muestra la barra de colores solo una vez al inicio
cv2.imshow('Rango de colores HSV', img)

# ---------- Bucle principal para video en vivo ----------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convierte el frame a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Crea una máscara con los valores del color definido
    mask = cv2.inRange(hsv, min_HSV, max_HSV)

    # Aplica la máscara al frame original
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Muestra las ventanas
    cv2.imshow('frame', frame)    # Imagen original
    cv2.imshow('mask', mask)      # Máscara binaria
    cv2.imshow('res', res)        # Resultado filtrado

    # Presiona ESC (27) para salir
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Libera recursos
cap.release()
cv2.destroyAllWindows()

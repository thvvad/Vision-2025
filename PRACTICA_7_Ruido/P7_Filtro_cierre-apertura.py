# P7: Cierre luego apertura

import cv2                     # Librería OpenCV para visión artificial
import numpy as np             # Librería NumPy para matrices y operaciones matemáticas

# Inicializar la cámara (índice 0 = cámara principal)
cap = cv2.VideoCapture(0)

# Definir el rango de color en RGB (ejemplo con rojo)
min_RGB = np.array([150, 0, 0])       # R: alto, G y B bajos (rojo oscuro)
max_RGB = np.array([255, 100, 100])   # Rojo claro sin llegar a rosa

# Convertir de RGB a BGR (porque OpenCV usa BGR)
bgr_min = min_RGB[::-1]  # [0, 0, 150]
bgr_max = max_RGB[::-1]  # [100, 100, 255]

# Función para crear una barra de color que representa el rango definido
def create_color_bar(min_color, max_color, width=300, height=50):
    bar = np.zeros((height, width, 3), dtype=np.uint8)  # Imagen negra
    for i in range(width):
        alpha = i / width  # Factor de interpolación de 0 a 1
        color = (1 - alpha) * min_color + alpha * max_color  # Color interpolado
        bar[:, i] = color  # Pintar la columna con el color correspondiente
    return bar.astype(np.uint8)

# Crear la barra de color
color_bar = create_color_bar(bgr_min, bgr_max)

# Bucle principal
while True:
    ret, frame = cap.read()  # Captura un frame de la cámara
    if not ret:
        break  # Si falla, termina el bucle

    # Crear máscara binaria con los píxeles dentro del rango
    mask = cv2.inRange(frame, bgr_min, bgr_max)

    # Aplicar la máscara cruda sobre el frame original
    res_crudo = cv2.bitwise_and(frame, frame, mask=mask)

    # Definir kernel para las operaciones morfológicas
    kernel = np.ones((4, 4), np.uint8)  # Matriz 4x4 de unos

    # --- NUEVO ORDEN: PRIMERO CIERRE, LUEGO APERTURA ---

    # CIERRE: rellena huecos negros dentro de las regiones blancas
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # APERTURA: elimina pequeños puntos blancos aislados (ruido)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)

    # Aplicar la máscara filtrada (final) al frame original
    result = cv2.bitwise_and(frame, frame, mask=opening)

    # Mostrar ventanas con cada paso
    cv2.imshow('Original', frame)              # Imagen de la cámara
    cv2.imshow('Mascara Cruda', mask)          # Máscara sin filtrar
    cv2.imshow('Crudo Aplicado', res_crudo)    # Imagen con máscara cruda
    cv2.imshow('Mascara Filtrada', opening)    # Máscara después de cierre + apertura
    cv2.imshow('Resultado', result)            # Imagen con máscara filtrada aplicada
    cv2.imshow('Color Range (RGB)', color_bar) # Rango de color como referencia

    # Esperar tecla (ESC = salir)
    key = cv2.waitKey(5) & 0xFF
    if key == 27:
        break

# Liberar cámara y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()

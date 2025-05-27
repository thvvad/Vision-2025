# Practica 7: Apertura luego cierre

import cv2                     # Librería OpenCV para visión artificial
import numpy as np             # Librería NumPy para matrices y operaciones matemáticas

# Inicializar la cámara (índice 0 = cámara principal)
cap = cv2.VideoCapture(0)

# Rango del color azul en RGB para facilitar comprensión (usuario)
#min_RGB = np.array([0, 0, 150])         # Azul oscuro
#max_RGB = np.array([80, 150, 250])     # Azul claro

# Filtro rojo
min_RGB = np.array([150, 0, 0])       # R: alto, G: bajo, B: bajo (rojo)
max_RGB = np.array([255, 100, 100])   # Hasta rojo más claro, sin llegar a rosa

# Convertir de RGB a BGR para usar en OpenCV
bgr_min = min_RGB[::-1]  # [150, 0, 0]
bgr_max = max_RGB[::-1]  # [255, 150, 150]

# Función para generar una barra de color que visualice el rango definido
def create_color_bar(min_color, max_color, width=300, height=50):
    bar = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(width):
        alpha = i / width  # interpolación lineal
        color = (1 - alpha) * min_color + alpha * max_color
        bar[:, i] = color
    return bar.astype(np.uint8)

# Generar la barra de color para mostrar el rango detectado
color_bar = create_color_bar(bgr_min, bgr_max)

# Bucle principal del programa
while True:
    ret, frame = cap.read()  # Captura un frame
    if not ret:
        break  # Si falla, se rompe el bucle

    # Crear la máscara binaria cruda según el rango definido
    mask = cv2.inRange(frame, bgr_min, bgr_max)

    # Aplicar la máscara cruda directamente sobre la imagen original
    res_crudo = cv2.bitwise_and(frame, frame, mask=mask)

    # Crear kernel (matriz de estructuración) para operaciones morfológicas
    kernel = np.ones((6, 6), np.uint8)

    # Apertura: elimina puntos blancos aislados (ruido)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Cierre: rellena huecos negros dentro de zonas blancas
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    # Aplicar la máscara filtrada sobre la imagen original
    result = cv2.bitwise_and(frame, frame, mask=closing)

    # Mostrar todas las ventanas:
    cv2.imshow('Original', frame)              # Imagen original de la cámara
    cv2.imshow('Mascara Cruda', mask)          # Mascara binaria sin filtrar
    cv2.imshow('Crudo Aplicado', res_crudo)    # Resultado con la mascara cruda
    cv2.imshow('Mascara Filtrada', closing)    # Mascara después de morfología
    cv2.imshow('Resultado', result)            # Imagen filtrada (después del ruido)
    cv2.imshow('Color Range (RGB)', color_bar) # Barra visual del rango de azul

    # Esperar tecla (ESC para salir)
    key = cv2.waitKey(5) & 0xFF
    if key == 27:
        break

# Liberar cámara y cerrar ventanas al finalizar
cap.release()
cv2.destroyAllWindows()

# Practica 7: Morfología con TopHat, Apertura, Cierre y BlackHat en orden personalizado

import cv2                      # Librería OpenCV para visión artificial
import numpy as np              # Librería NumPy para manejo de matrices

# Inicializar la cámara principal
cap = cv2.VideoCapture(0)

# Rango de azul definido en RGB
min_RGB = np.array([0, 0, 150])
max_RGB = np.array([80, 150, 250])

# Convertir RGB a BGR (OpenCV usa BGR)
bgr_min = min_RGB[::-1]
bgr_max = max_RGB[::-1]

# Crear barra de colores para mostrar rango
def create_color_bar(min_color, max_color, width=300, height=50):
    bar = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(width):
        alpha = i / width
        color = (1 - alpha) * min_color + alpha * max_color
        bar[:, i] = color
    return bar.astype(np.uint8)

color_bar = create_color_bar(bgr_min, bgr_max)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 1. Crear máscara binaria cruda (donde el color azul esté dentro del rango)
    mask = cv2.inRange(frame, bgr_min, bgr_max)

    # 2. Aplicar máscara cruda directamente a la imagen
    res_crudo = cv2.bitwise_and(frame, frame, mask=mask)

    # 3. Crear kernel estructurante
    kernel = np.ones((6, 6), np.uint8)

    # 4. Aplicar MORPH_TOPHAT (resalta detalles blancos pequeños)
    step1_tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)

    # 5. Aplicar apertura para eliminar puntos blancos fuera del objeto
    step2_open = cv2.morphologyEx(step1_tophat, cv2.MORPH_OPEN, kernel)

    # 6. Aplicar cierre para rellenar puntos negros dentro del objeto
    step3_close = cv2.morphologyEx(step2_open, cv2.MORPH_CLOSE, kernel)

    # 7. Aplicar MORPH_BLACKHAT sobre el resultado anterior (resalta manchas negras restantes)
    step4_blackhat = cv2.morphologyEx(step3_close, cv2.MORPH_BLACKHAT, kernel)

    # 8. Aplicar la máscara final (tras todas las operaciones) al frame original
    resultado_final = cv2.bitwise_and(frame, frame, mask=step4_blackhat)

    # Mostrar todas las ventanas
    cv2.imshow('Original', frame)
    cv2.imshow('Mascara Cruda', mask)
    cv2.imshow('Crudo Aplicado', res_crudo)
    cv2.imshow('TopHat aplicado', step1_tophat)
    cv2.imshow('Tras Apertura', step2_open)
    cv2.imshow('Tras Cierre', step3_close)
    cv2.imshow('Final (BlackHat)', step4_blackhat)
    cv2.imshow('Resultado Final con Mascara BlackHat', resultado_final)
    cv2.imshow('Color Range (RGB)', color_bar)

    # Tecla ESC para salir
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()

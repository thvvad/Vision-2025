# Practica 7: Morfología con suma de TopHat y BlackHat antes del cierre y apertura

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

    # 1. Máscara cruda (blanco donde hay azul)
    mask = cv2.inRange(frame, bgr_min, bgr_max)

    # 2. Aplicar máscara cruda directamente
    res_crudo = cv2.bitwise_and(frame, frame, mask=mask)

    # 3. Crear kernel estructurante
    kernel = np.ones((6, 6), np.uint8)

    # 4. TopHat y BlackHat desde la máscara cruda (antes de cierre y apertura)
    tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
    blackhat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)

    # 5. Sumar TopHat y BlackHat a la máscara cruda
    mascara_mejorada = cv2.add(mask, tophat)
    mascara_mejorada = cv2.add(mascara_mejorada, blackhat)

    # 6. Aplicar cierre + apertura a la máscara mejorada
    closing = cv2.morphologyEx(mascara_mejorada, cv2.MORPH_CLOSE, kernel)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)

    # 7. Aplicar solo la máscara filtrada (opening) a la imagen original
    resultado_filtrado = cv2.bitwise_and(frame, frame, mask=opening)

    # 8. Aplicar la máscara mejorada (después de cierre + apertura) al frame
    resultado_final = cv2.bitwise_and(frame, frame, mask=opening)

    # Mostrar ventanas
    cv2.imshow('Original', frame)
    cv2.imshow('Mascara Cruda', mask)
    cv2.imshow('Crudo Aplicado', res_crudo)
    cv2.imshow('Mascara Mejorada (Cruda+TopHat+BlackHat)', mascara_mejorada)
    #cv2.imshow('Mascara Filtrada (Cierre + Apertura)', opening)
    #cv2.imshow('Resultado Solo con Mascara Filtrada', resultado_filtrado)
    #cv2.imshow('TopHat (blancos pequeños)', tophat)
    #cv2.imshow('BlackHat (negros pequeños)', blackhat)
    cv2.imshow('Resultado Final', resultado_final)
    cv2.imshow('Color Range (RGB)', color_bar)

    # Tecla ESC para salir
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()

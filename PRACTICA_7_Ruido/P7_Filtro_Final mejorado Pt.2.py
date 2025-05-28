import cv2
import numpy as np

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Rango de azul definido en RGB (más intuitivo para ti)
min_RGB = np.array([0, 0, 150])
max_RGB = np.array([80, 150, 250])

# Convertir a BGR (formato que usa OpenCV)
bgr_min = min_RGB[::-1]
bgr_max = max_RGB[::-1]

# Crear barra visual del rango de color
def create_color_bar(min_color, max_color, width=300, height=50):
    bar = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(width):
        alpha = i / width
        color = (1 - alpha) * min_color + alpha * max_color
        bar[:, i] = color
    return bar.astype(np.uint8)

color_bar = create_color_bar(bgr_min, bgr_max)

# Bucle principal
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Crear máscara cruda desde la imagen original
    mask = cv2.inRange(frame, bgr_min, bgr_max)

    # Aplicar la máscara cruda a la imagen original
    res_crudo = cv2.bitwise_and(frame, frame, mask=mask)

    # Crear kernel para operaciones morfológicas
    kernel = np.ones((6, 6), np.uint8)

    # === ORDEN: TopHat → Cierre → BlackHat ===

    # 1. TopHat sobre la máscara cruda
    tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)

    # 2. Cierre aplicado a la imagen resultante del TopHat
    closing = cv2.morphologyEx(tophat, cv2.MORPH_CLOSE, kernel)

    # 3. BlackHat sobre la imagen del cierre
    blackhat = cv2.morphologyEx(closing, cv2.MORPH_BLACKHAT, kernel)

    # 4. Resultado final: aplicar esta máscara (blackhat) al frame
    resultado_final = cv2.bitwise_and(frame, frame, mask=blackhat)

    # Mostrar todas las ventanas
    cv2.imshow('Original', frame)
    cv2.imshow('Mascara Cruda', mask)
    cv2.imshow('Crudo Aplicado', res_crudo)
    #cv2.imshow('TopHat', tophat)
    cv2.imshow('Cierre (después de TopHat)', closing)
    cv2.imshow('BlackHat (después de Cierre)', blackhat)
    cv2.imshow('Resultado Final', resultado_final)
    cv2.imshow('Color Range (RGB)', color_bar)

    # Salir con ESC
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()

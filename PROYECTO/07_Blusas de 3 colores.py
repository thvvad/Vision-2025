# Proyecto: Deteccion de blusas de 3 colores distintos

import cv2
import numpy as np
from tensorflow.keras.models import load_model

# ---------------------- CARGA DE MODELO ----------------------
modelo = load_model('mnist-fashion-model.h5')

etiquetas = {
    0: 'camiseta/blusa',
    6: 'camisa'
}

# ---------------------- FUNCIÓN: BARRA DE COLOR ----------------------
def create_color_bar(min_color, max_color, width=300, height=50):
    bar = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(width):
        alpha = i / width
        color = (1 - alpha) * min_color + alpha * max_color
        bar[:, i] = color
    return bar.astype(np.uint8)

# ---------------------- FUNCIÓN DE DETECCIÓN ----------------------
def detectar_camisas_por_color(frame_original, min_RGB, max_RGB, color_rectangulo, nombre_mascara, nombre_barra):
    frame_resultado = frame_original.copy()

    bgr_min = min_RGB[::-1]
    bgr_max = max_RGB[::-1]

    mask = cv2.inRange(frame_original, bgr_min, bgr_max)
    mask_original = mask.copy()

    # Mejora morfológica
    kernel = np.ones((3, 3), np.uint8)
    tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
    blackhat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)
    mascara_mejorada = cv2.add(mask, tophat)
    mascara_mejorada = cv2.add(mascara_mejorada, blackhat)
    closing = cv2.morphologyEx(mascara_mejorada, cv2.MORPH_CLOSE, kernel)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)

    contornos, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Máscara convertida a color para dibujar las ROIs
    mascara_con_rois = cv2.cvtColor(mask_original, cv2.COLOR_GRAY2BGR)

    for contorno in contornos:
        x, y, w, h = cv2.boundingRect(contorno)
        if w < 20 or h < 20:
            continue

        # Dibujar rectángulo en máscara
        cv2.rectangle(mascara_con_rois, (x, y), (x + w, y + h), (255, 255, 255), 2)

        roi_color = frame_original[y:y + h, x:x + w]
        roi_gray = cv2.cvtColor(roi_color, cv2.COLOR_BGR2GRAY)
        h_roi, w_roi = roi_gray.shape
        scale = 20.0 / max(w_roi, h_roi)
        resized = cv2.resize(roi_gray, (int(w_roi * scale), int(h_roi * scale)))
        roi_final = np.zeros((28, 28), dtype=np.uint8)
        x_offset = (28 - resized.shape[1]) // 2
        y_offset = (28 - resized.shape[0]) // 2
        roi_final[y_offset:y_offset + resized.shape[0], x_offset:x_offset + resized.shape[1]] = resized
        roi_final = cv2.bitwise_not(roi_final)
        roi_normalizado = roi_final.astype(np.float32) / 255.0
        entrada = roi_normalizado.reshape(1, 28, 28, 1)

        prediccion = modelo.predict(entrada)
        clase = np.argmax(prediccion)

        if clase in [0, 6]:
            etiqueta = etiquetas.get(clase, 'camisa/blusa')
            cv2.rectangle(frame_resultado, (x, y), (x + w, y + h), color_rectangulo, 2)
            cv2.putText(frame_resultado, etiqueta, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color_rectangulo, 1)

    # Mostrar la máscara con ROIs
    cv2.imshow(f"Mascara {nombre_mascara}", mascara_con_rois)

    # Mostrar la barra de color en ventana separada
    color_bar = create_color_bar(bgr_min, bgr_max)
    cv2.imshow(f"Rango {nombre_barra}", color_bar)

    return frame_resultado

# ---------------------- CARGA DE IMAGEN ----------------------
frame = cv2.imread('ropa2.jpg')
if frame is None:
    print("No se pudo cargar la imagen.")
    exit()

# ---------------------- DETECCIÓN POR COLORES ----------------------
frame = detectar_camisas_por_color(
    frame_original=frame,
    min_RGB=np.array([120, 0, 0]),
    max_RGB=np.array([255, 80, 80]),
    color_rectangulo=(0, 0, 255),
    nombre_mascara='Roja',
    nombre_barra='Rojo'
)

frame = detectar_camisas_por_color(
    frame_original=frame,
    min_RGB=np.array([0, 0, 120]),
    max_RGB=np.array([80, 80, 255]),
    color_rectangulo=(255, 0, 0),
    nombre_mascara='Azul',
    nombre_barra='Azul'
)

frame = detectar_camisas_por_color(
    frame_original=frame,
    min_RGB=np.array([0, 120, 0]),
    max_RGB=np.array([80, 255, 80]),
    color_rectangulo=(0, 255, 0),
    nombre_mascara='Verde',
    nombre_barra='Verde'
)

# ---------------------- RESULTADO FINAL ----------------------
cv2.imshow("Detección Final", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

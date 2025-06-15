import cv2
import numpy as np
from tensorflow.keras.models import load_model

# ---------------------- CARGA DE MODELO ----------------------
# Cargar el modelo previamente entrenado
modelo = load_model('mnist-fashion-model.h5')

# Etiquetas según Fashion MNIST (solo usamos algunas)
etiquetas = {
    0: 'camiseta/blusa',  # RECTÁNGULO VERDE
    1: 'pantalón',        # RECTÁNGULO MORADO
    2: 'suéter',          # (opcional)
    3: 'vestido',         # RECTÁNGULO AZUL
    4: 'abrigo',          # (opcional)
    5: 'sandalia',        # RECTÁNGULO NEGRO (zapato)
    6: 'camisa',          # RECTÁNGULO VERDE
    7: 'zapatilla',       # RECTÁNGULO NEGRO (zapato)
    8: 'bolsa',           # ignorar
    9: 'botín'            # RECTÁNGULO NEGRO (zapato)
}

# ---------------------- FILTRO DE COLOR ROJO ----------------------
# Cargar imagen desde archivo
frame = cv2.imread('ropa.jpg')
if frame is None:
    print("No se pudo cargar la imagen.")
    exit()

# Definir el rango de color rojo en formato BGR
min_RGB = np.array([120, 0, 0])
max_RGB = np.array([255, 80, 80])
bgr_min = min_RGB[::-1]
bgr_max = max_RGB[::-1]

# Crear máscara binaria para el color rojo
mask = cv2.inRange(frame, bgr_min, bgr_max)

# Mejorar la máscara usando morfología
kernel = np.ones((3, 3), np.uint8)
tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)
mascara_mejorada = cv2.add(mask, tophat)
mascara_mejorada = cv2.add(mascara_mejorada, blackhat)
closing = cv2.morphologyEx(mascara_mejorada, cv2.MORPH_CLOSE, kernel)
opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)

# ---------------------- DETECCIÓN DE CONTORNOS ----------------------
# Encontrar los contornos de las regiones rojas detectadas
contornos, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Recorrer cada contorno encontrado
for contorno in contornos:
    x, y, w, h = cv2.boundingRect(contorno)
    
    # Ignorar regiones muy pequeñas (ruido)
    if w < 20 or h < 20:
        continue

    # Extraer ROI de la imagen original
    roi_color = frame[y:y+h, x:x+w]

    # ---------------------- PREPROCESAMIENTO PARA EL MODELO ----------------------
    # 1. Convertir a escala de grises
    roi_gray = cv2.cvtColor(roi_color, cv2.COLOR_BGR2GRAY)

    # 2. Redimensionar manteniendo proporción con padding (a 28x28)
    h_roi, w_roi = roi_gray.shape
    scale = 20.0 / max(w_roi, h_roi)
    resized = cv2.resize(roi_gray, (int(w_roi * scale), int(h_roi * scale)))

    # 3. Centrar la ROI redimensionada en un lienzo negro de 28x28
    roi_final = np.zeros((28, 28), dtype=np.uint8)
    x_offset = (28 - resized.shape[1]) // 2
    y_offset = (28 - resized.shape[0]) // 2
    roi_final[y_offset:y_offset+resized.shape[0], x_offset:x_offset+resized.shape[1]] = resized

    # 4. Invertir colores (Fashion MNIST tiene fondo negro y prenda blanca)
    roi_final = cv2.bitwise_not(roi_final)

    # 5. Normalizar a rango [0, 1]
    roi_normalizado = roi_final.astype(np.float32) / 255.0

    # 6. Convertir al formato que espera el modelo
    entrada = roi_normalizado.reshape(1, 28, 28, 1)

    # ---------------------- PREDICCIÓN ----------------------
    prediccion = modelo.predict(entrada)
    clase = np.argmax(prediccion)

    etiqueta = etiquetas.get(clase, 'otro')

    # ---------------------- DIBUJAR RECTÁNGULOS SEGÚN CLASE ----------------------
    color = None
    if clase in [5, 7, 9]:       # Zapatos
        color = (0, 0, 0)        # Negro
    elif clase == 3:             # Vestido
        color = (255, 0, 0)      # Azul (BGR)
    elif clase in [0, 6]:        # Camisas
        color = (0, 255, 0)      # Verde
    elif clase == 1:             # Pantalón
        color = (255, 0, 255)    # Morado
    else:
        color = None             # Ignorar otras clases

    # Si es una clase válida, dibujar el rectángulo
    if color:
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        # Mostrar etiqueta encima del rectángulo (opcional)
        cv2.putText(frame, etiqueta, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

# ---------------------- MOSTRAR RESULTADO FINAL ----------------------
cv2.imshow("Detección de Prendas Rojas", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2                      # Librería OpenCV para visión artificial
import numpy as np              # Librería NumPy para manejo de matrices

# Cargar imagen desde archivo (cambia el nombre si es necesario)
frame = cv2.imread('ropa.jpg')   # Carga una imagen .jpg del disco

# Verifica que la imagen haya cargado correctamente
if frame is None:
    print("No se pudo cargar la imagen.")
    exit()

# Rango de rojo definido en RGB (color R:234, G:55, B:26 con tolerancia ±20)
min_RGB = np.array([120, 0, 0])
max_RGB = np.array([255, 80, 80])

# Convertir de RGB a BGR (OpenCV trabaja con BGR)
bgr_min = min_RGB[::-1]   # => [6, 35, 214]
bgr_max = max_RGB[::-1]   # => [46, 75, 254]

# Crear barra de colores para mostrar el rango de color seleccionado
def create_color_bar(min_color, max_color, width=300, height=50):
    bar = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(width):
        alpha = i / width
        color = (1 - alpha) * min_color + alpha * max_color
        bar[:, i] = color
    return bar.astype(np.uint8)

color_bar = create_color_bar(bgr_min, bgr_max)

# 1. Crear una máscara binaria con los píxeles dentro del rango BGR
mask = cv2.inRange(frame, bgr_min, bgr_max)

# 2. Aplicar la máscara cruda directamente a la imagen
res_crudo = cv2.bitwise_and(frame, frame, mask=mask)

# 3. Crear kernel estructurante para operaciones morfológicas
kernel = np.ones((1, 1), np.uint8)

# 4. Aplicar TopHat y BlackHat sobre la máscara
tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)

# 5. Sumar TopHat y BlackHat a la máscara original
mascara_mejorada = cv2.add(mask, tophat)
mascara_mejorada = cv2.add(mascara_mejorada, blackhat)

# 6. Realizar cierre seguido de apertura (elimina ruido)
closing = cv2.morphologyEx(mascara_mejorada, cv2.MORPH_CLOSE, kernel)
opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)

# 7. Aplicar la máscara final filtrada a la imagen original
resultado_final = cv2.bitwise_and(frame, frame, mask=opening)

# 8. Mostrar resultados en distintas ventanas
cv2.imshow('Original', frame)
cv2.imshow('Mascara Cruda', mask)
cv2.imshow('Crudo Aplicado', res_crudo)
cv2.imshow('Mascara Mejorada (Cruda+TopHat+BlackHat)', mascara_mejorada)
cv2.imshow('Mascara Filtrada (Cierre + Apertura)', opening)
cv2.imshow('Resultado Final', resultado_final)
cv2.imshow('Color Range (RGB)', color_bar)

# Espera hasta que se presione una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()

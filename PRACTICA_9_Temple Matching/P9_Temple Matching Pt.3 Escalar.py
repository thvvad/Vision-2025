# Practica #9: Temple Matching ´para mismo objeto, diferente escala
import cv2
import numpy as np

# Cargar imagen original a color
img_rgb = cv2.imread('tri.jpg')
img_display = img_rgb.copy()

# Selección manual de la plantilla
roi = cv2.selectROI("Selecciona la plantilla", img_display)
template = img_rgb[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Convertimos imagen original a escala de grises
img_gray_original = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

threshold = 0.8  # Umbral de coincidencia
scales = np.linspace(0.5, 2, 50)  # Escalas de 50% a 150%, con 20 pasos

# Para cada escala
for scale in scales:
    # Escalamos la imagen original
    resized = cv2.resize(img_gray_original, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)

    # Si la imagen escalada es más pequeña que la plantilla, ya no tiene sentido continuar
    if resized.shape[0] < template_gray.shape[0] or resized.shape[1] < template_gray.shape[1]:
        continue

    # Aplicamos template matching
    res = cv2.matchTemplate(resized, template_gray, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    # Por cada coincidencia, calculamos la posición en la imagen original
    for pt in zip(*loc[::-1]):
        top_left = (int(pt[0] / scale), int(pt[1] / scale))
        bottom_right = (int((pt[0] + template_gray.shape[1]) / scale),
                        int((pt[1] + template_gray.shape[0]) / scale))
        cv2.rectangle(img_rgb, top_left, bottom_right, (0, 255, 255), 2)

# Mostrar resultado
cv2.imshow('Detected at Multiple Scales', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Practica 9: Temple Matching

import cv2 # Se importa la librería OpenCV, usada para procesamiento de imágenes

import numpy as np # Se importa NumPy, usada aquí para manejar arreglos (matrices de imágenes)

# Se lee la imagen principal (a color), en la que se buscará una subimagen o plantilla
img_rgb = cv2.imread('opencv-template-matching-python-tutorial.jpg')

# Se convierte la imagen principal a escala de grises, ya que la coincidencia se hace sobre imágenes en gris
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

# Fragmento que queremos encontrar en escala de grises (el '0' indica eso)
template = cv2.imread('opencv-template-for-matching.jpg',0)

w, h = template.shape[::-1]     # Se obtienen el ancho y alto de la imagen plantilla
# El [::-1] invierte el orden porque `shape` devuelve (alto, ancho), pero necesitamos (ancho, alto)

# Se aplica la función de coincidencia de plantillas, comparando la imagen con la plantilla
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
# El método `cv2.TM_CCOEFF_NORMED` compara cuán similares son los patrones normalizados

# Se define un umbral de similitud. Solo coincidencias con valor >= 0.8 serán consideradas válidas
threshold = 0.8
# 0.7 para un rango mas abierto

# Se obtienen las coordenadas (x, y) donde el valor de coincidencia es mayor o igual al umbral
loc = np.where( res >= threshold)

# Para cada coincidencia:
for pt in zip(*loc[::-1]):
    # `zip(*loc[::-1])` transforma las coordenadas en puntos (x, y)
    
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
    # Se dibuja un rectángulo en la imagen original (a color) en cada coincidencia encontrada
    # pt es la esquina superior izquierda, (pt[0] + w, pt[1] + h) es la esquina inferior derecha
    # (0,255,255) es el color del rectángulo (amarillo en BGR), y 2 es el grosor de línea

cv2.imshow('Detected',img_rgb)
# Se muestra en pantalla la imagen original con los rectángulos dibujados donde se detectó la plantilla


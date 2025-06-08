# Practica 10: Detección de esquinas solo en una ROI y visualización con fondo negro conservando los puntos

import numpy as np
import cv2

# Carga la imagen original
img = cv2.imread('figuras.jpg')

# Crea una imagen negra del mismo tamaño para mostrar solo la ROI
mascara_negra = np.zeros_like(img)

# Permite al usuario seleccionar la Región de Interés (ROI)
x, y, w, h = cv2.selectROI("Selecciona una región", img)

# Extrae la ROI de la imagen original
roi = img[y:y+h, x:x+w]

# Convierte la ROI a escala de grises
gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

# Convierte la imagen a float32 para la detección de esquinas
gray = np.float32(gray)

# Aplica el detector de esquinas Shi-Tomasi en la ROI
corners = cv2.goodFeaturesToTrack(gray, 100, 0.1, 10)

# Si se detectaron esquinas:
if corners is not None:
    corners = np.int0(corners)
    
    for corner in corners:
        # Coordenadas relativas a la ROI
        x_roi, y_roi = corner.ravel()
        # Coordenadas absolutas dentro de la imagen original
        x_img = x + x_roi
        y_img = y + y_roi
        # Dibuja el punto blanco directamente en la máscara negra
        cv2.circle(mascara_negra, (x_img, y_img), 3, (255, 255, 255), -1)

# Copia la ROI original (solo imagen, sin sobrescribir los puntos) a su posición correspondiente en la máscara
mascara_negra[y:y+h, x:x+w] = img[y:y+h, x:x+w]

# Vuelve a dibujar los puntos después de copiar la imagen para que no se borren
if corners is not None:
    for corner in corners:
        x_roi, y_roi = corner.ravel()
        x_img = x + x_roi
        y_img = y + y_roi
        cv2.circle(mascara_negra, (x_img, y_img), 3, (0, 0, 255), -1)

# Muestra la imagen con fondo negro y esquinas detectadas en la ROI
cv2.imshow('ROI con esquinas (fondo negro)', mascara_negra)

# Espera a que se presione una tecla para cerrar
cv2.waitKey(0)
cv2.destroyAllWindows()

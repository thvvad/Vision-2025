# Practica 10: Detección de esquinas en una ROI seleccionada manualmente

import numpy as np
import cv2

# Carga la imagen original
img = cv2.imread('figuras.jpg')

# Crea una imagen negra del mismo tamaño
mascara_negra = np.zeros_like(img)

# Permite seleccionar la región de interés (ROI)
x, y, w, h = cv2.selectROI("Selecciona una region", img)

# Extrae la ROI
roi = img[y:y+h, x:x+w]

# Convierte la ROI a escala de grises
roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

# Aplica umbralización binaria (blanco y negro)
_, roi_bin = cv2.threshold(roi_gray, 150, 255, cv2.THRESH_BINARY)

# Convierte la imagen umbralizada a 3 canales para poder insertarla de nuevo
roi_bin_color = cv2.cvtColor(roi_bin, cv2.COLOR_GRAY2BGR)

# Aplica detección de esquinas en la imagen umbralizada
gray_float = np.float32(roi_bin)  # convertir a float32 para goodFeaturesToTrack
corners = cv2.goodFeaturesToTrack(gray_float, 30, 0.1, 10)

# Dibuja los puntos detectados directamente sobre la ROI en blanco y negro
if corners is not None:
    corners = np.int0(corners)
    for corner in corners:
        x_r, y_r = corner.ravel()
        cv2.circle(roi_bin_color, (x_r, y_r), 3, (0, 0, 255), -1)

# Inserta la ROI procesada (con umbral y esquinas) en su lugar dentro de la imagen negra
mascara_negra[y:y+h, x:x+w] = roi_bin_color

# Muestra la imagen final: solo la ROI en B/N y esquinas visibles, lo demás en negro
cv2.imshow('ROI binarizada con esquinas (fondo negro)', mascara_negra)

# Espera a que se presione una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()

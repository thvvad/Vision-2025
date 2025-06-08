# Elimina el fondo y solo deja el objeto que se esta moviendo

import numpy as np
import cv2

# Captura de video desde la cámara (índice 0)
cap = cv2.VideoCapture(0)

# Creador de sustractor de fondo MOG2
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    # Captura un nuevo cuadro de la cámara
    ret, frame = cap.read()

    # Verifica si el cuadro fue capturado correctamente
    if not ret:
        break

    # Aplica el sustractor de fondo y obtiene la máscara (blanco: movimiento, negro: fondo)
    fgmask = fgbg.apply(frame)

    # Aplica la máscara sobre la imagen original usando bitwise_and
    masked_frame = cv2.bitwise_and(frame, frame, mask=fgmask)

    # Muestra el cuadro original
    cv2.imshow('Imagen Original', frame)

    # Muestra la máscara (blanco = movimiento)
    cv2.imshow('Mascara (Movimiento Detectado)', fgmask)

    # Muestra la imagen original con la máscara aplicada
    cv2.imshow('Mascara Aplicada a la Imagen', masked_frame)

    # Espera 30 ms por una tecla. Si es Esc (27), se sale del bucle
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Libera la cámara
cap.release()

# Cierra todas las ventanas de OpenCV
cv2.destroyAllWindows()


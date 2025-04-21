# Practica 6: Filtros de color

import cv2  # Importa la librería OpenCV para procesamiento de imágenes y video
import numpy as np  # Importa NumPy para manejo de arreglos y operaciones numéricas

cap = cv2.VideoCapture(0)  # Abre la cámara web (índice 0 es la cámara por defecto)

while(1):  # Inicia un bucle infinito para capturar video en tiempo real
    _, frame = cap.read()  # Lee un frame (imagen) desde la cámara

    # Convierte el frame de formato BGR (por defecto en OpenCV) a HSV (tono, saturación, valor)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define los límites inferior y superior del color a detectar en espacio HSV
    lower_red = np.array([30, 150, 50])  # Límite inferior del rango (no es rojo puro)
    upper_red = np.array([255, 255, 180])  # Límite superior del rango

    # Crea una máscara binaria donde los colores dentro del rango son blancos (255), el resto negros (0)
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Aplica la máscara a la imagen original, resaltando solo los píxeles dentro del rango de color
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Muestra la imagen original en una ventana llamada 'frame'
    cv2.imshow('frame', frame)

    # Muestra la máscara en blanco y negro en una ventana llamada 'mask'
    cv2.imshow('mask', mask)

    # Muestra el resultado final con el color filtrado resaltado en una ventana llamada 'res'
    cv2.imshow('res', res)

    # Espera 5 milisegundos por una tecla. Si se presiona 'Esc' (código 27), se rompe el bucle
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# Cierra todas las ventanas abiertas
cv2.destroyAllWindows()

# Libera la cámara
cap.release()

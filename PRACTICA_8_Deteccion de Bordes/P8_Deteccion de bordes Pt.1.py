# Practica 8: Deteccion de bordes Pt.1
# Laplaciano, Sobelx, Sobely

import cv2                   # Importa la librería OpenCV para procesamiento de imágenes y video.
import numpy as np           # Importa NumPy para operaciones numéricas con arrays, útil para manejar matrices de imágenes.

cap = cv2.VideoCapture(0)    # Crea un objeto que captura video desde la cámara con índice 1.
                             # (Puede que necesites usar 0 en algunas computadoras si la cámara principal es la que deseas.)

while(1):                    # Bucle infinito que se ejecuta continuamente para capturar y procesar cada frame.

    # Captura un frame del video
    _, frame = cap.read()    # Lee un frame de la cámara. `_` ignora el valor de retorno de éxito; `frame` es la imagen capturada.

    # Convierte la imagen capturada de BGR (azul, verde, rojo) a HSV (tono, saturación, valor)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define un rango inferior y superior para un color en el espacio HSV (aquí parece ser un color rojo anaranjado)
    lower_red = np.array([30,150,50])     # Límite inferior del color que se quiere detectar (tono claro).
    upper_red = np.array([255,255,180])   # Límite superior del color.

    # Crea una máscara que deja pasar solo los pixeles dentro del rango de color definido
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Aplica la máscara sobre la imagen original para resaltar solo las áreas con el color seleccionado
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Aplica el filtro de Laplace para detectar bordes (derivadas de segundo orden)
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)  # Usa precisión de 64 bits para evitar pérdida de información.

    # Aplica el filtro Sobel en dirección X (horizontal)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    # Parámetros:
    # - 1 y 0 indican que se toma la derivada en x, no en y.
    # - ksize=5 es el tamaño del kernel (más grande = más suavizado)

    # Aplica el filtro Sobel en dirección Y (vertical)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

    # Muestra la imagen original
    cv2.imshow('Original', frame)

    # Muestra la máscara en blanco y negro (zonas que cumplen con el color definido)
    cv2.imshow('Mask', mask)

    # Muestra el resultado del filtro de Laplace (bordes detectados)
    cv2.imshow('laplacian', laplacian)

    # Muestra los bordes detectados en dirección horizontal
    cv2.imshow('sobelx', sobelx)

    # Muestra los bordes detectados en dirección vertical
    cv2.imshow('sobely', sobely)

    # Espera 5 milisegundos por una tecla; si es la tecla Esc (código ASCII 27), se sale del bucle
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# Cierra todas las ventanas creadas por OpenCV
cv2.destroyAllWindows()

# Libera la cámara para que otros programas puedan usarla
cap.release()

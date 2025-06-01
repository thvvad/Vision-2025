# Practica 8: Detección de bordes - Escala de grises + Filtro Gaussiano + Sobel X/Y

import cv2                   # Librería de visión artificial OpenCV
import numpy as np           # Librería para trabajar con matrices

cap = cv2.VideoCapture(0)    # Inicia la captura de video desde la cámara principal (índice 0)

while(1):                    # Bucle infinito para capturar y procesar cada frame

    ret, frame = cap.read()  # Lee un frame de la cámara. 'ret' indica si fue exitoso, 'frame' es la imagen capturada
    if not ret:              # Si no se capturó correctamente, se salta esta vuelta del bucle
        continue

    # Muestra la imagen original capturada desde la cámara
    cv2.imshow('Original', frame)

    # Convierte la imagen BGR a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gris', gray)  # Muestra la imagen en escala de grises

    # Aplica un filtro Gaussiano para suavizar y reducir ruido
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)  # (5,5): tamaño del kernel; 0: desviación estándar automática
    cv2.imshow('Filtro Gaussiano', blurred)      # Muestra la imagen suavizada

    # Aplica el filtro Sobel en dirección X (detecta bordes verticales)
    sobelx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=5)
    cv2.imshow('Sobel X', sobelx)  # Muestra bordes detectados en X

    # Aplica el filtro Sobel en dirección Y (detecta bordes horizontales)
    sobely = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=5)
    cv2.imshow('Sobel Y', sobely)  # Muestra bordes detectados en Y

    # Suma ambos resultados para obtener bordes completos en todas direcciones
    sobel_combined = cv2.add(np.abs(sobelx), np.abs(sobely))  # np.abs para convertir valores negativos a positivos
    sobel_combined = np.uint8(sobel_combined)  # Convierte a formato de imagen de 8 bits
    cv2.imshow('Sobel Combinado', sobel_combined)  # Muestra el resultado final

    # Espera una tecla por 5 ms; si es ESC (27), rompe el bucle
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Libera los recursos de la cámara y cierra ventanas
cap.release()
cv2.destroyAllWindows()

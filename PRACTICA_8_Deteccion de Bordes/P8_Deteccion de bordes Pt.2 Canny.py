# Practica 8: Deteccion de bordes Pt.2: Canny

import cv2                  # Importa la librería OpenCV, que se usa para procesar imágenes y video.
import numpy as np          # Importa NumPy para manipular matrices (arrays), útil para definir rangos de color.

cap = cv2.VideoCapture(0)   # Inicializa la captura de video desde la cámara con índice 0 (cámara principal).

while(1):                   # Inicia un bucle infinito para procesar video en tiempo real.

    # Captura un frame de la cámara
    _, frame = cap.read()   # 'frame' contiene la imagen capturada. El primer valor se ignora con '_'.

    # Convierte la imagen de formato BGR (por defecto en OpenCV) a HSV (tono, saturación, valor).
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define un rango inferior del color (valores de tono, saturación y brillo).
    lower_red = np.array([30,150,50])     # Tono bajo para detectar un color rojizo/naranja.
    upper_red = np.array([255,255,180])   # Tono alto para limitar el rango.

    # Crea una máscara en blanco y negro: blanco para pixeles dentro del rango, negro para los demás.
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Aplica la máscara a la imagen original. Solo se mantienen los píxeles en el rango de color definido.
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Muestra la imagen original capturada de la cámara.
    cv2.imshow('Original', frame)

    # Aplica el detector de bordes de Canny. Detecta contornos en la imagen original.
    edges = cv2.Canny(frame, 100, 200)
    # - 100: umbral inferior para detectar bordes.
    # - 200: umbral superior.

    # Muestra la imagen con los bordes detectados.
    cv2.imshow('Edges', edges)

    # Espera 5 milisegundos a que se presione una tecla.
    # Si se presiona la tecla 'Esc' (código ASCII 27), se sale del bucle.
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# Cierra todas las ventanas que fueron abiertas con imshow()
cv2.destroyAllWindows()

# Libera la cámara para que pueda ser usada por otros programas.
cap.release()

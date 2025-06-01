# Detección de bordes con Sobel, umbralización y operación NAND + control de contraste manual

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# -------------------
# Variable de control de contraste (ajústala a tu gusto)
contraste_manual = 2  # Valor mayor a 1 aumenta contraste; entre 0 y 1 lo reduce
# -------------------

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    cv2.imshow('Original', frame)

    # 1. Escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gris', gray)

    # 2. Ecualización del histograma
    equalized = cv2.equalizeHist(gray)

    # 3. Ajuste manual de contraste (después de ecualizar)
    # Formula: salida = imagen * alpha + beta, aquí beta = 0
    contrasted = cv2.convertScaleAbs(equalized, alpha=contraste_manual, beta=0)
    cv2.imshow('Ecualizada + Contraste', contrasted)

    # 4. Sobel X
    sobelx = cv2.Sobel(contrasted, cv2.CV_64F, 1, 0, ksize=5)
    sobelx_abs = cv2.convertScaleAbs(sobelx)

    # 5. Sobel Y
    sobely = cv2.Sobel(contrasted, cv2.CV_64F, 0, 1, ksize=5)
    sobely_abs = cv2.convertScaleAbs(sobely)

    # 6. Umbralización
    _, sobelx_thresh = cv2.threshold(sobelx_abs, 253, 255, cv2.THRESH_BINARY)
    _, sobely_thresh = cv2.threshold(sobely_abs, 253, 255, cv2.THRESH_BINARY)
    cv2.imshow('Sobel X (thresh)', sobelx_thresh)
    cv2.imshow('Sobel Y (thresh)', sobely_thresh)

    # 7. Operación NAND = NOT(AND)
    and_result = cv2.bitwise_and(sobelx_thresh, sobely_thresh)
    nand_result = cv2.bitwise_not(and_result)
    cv2.imshow('Sobel NAND (final)', nand_result)

    # 8. Salida
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

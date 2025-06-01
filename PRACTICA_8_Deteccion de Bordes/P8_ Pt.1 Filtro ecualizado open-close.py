# Detección de bordes con ajuste manual de contraste y umbral de Sobel
# Por Vanessa Aguirre

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Parámetros ajustables:
contraste_manual = 1     # Aumenta o disminuye el contraste de la imagen ecualizada
umbral_sobel = 250         # Umbral para binarizar Sobel X y Y (ajústalo según el ruido o definición deseada)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # 1. Mostrar imagen original
    cv2.imshow('Original', frame)

    # 2. Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gris', gray)

    # 3. Ecualizar histograma para aumentar contraste
    equalized = cv2.equalizeHist(gray)

    # 4. Aplicar aumento de contraste con variable manual
    contrasted = cv2.convertScaleAbs(equalized, alpha=contraste_manual, beta=0)
    cv2.imshow('Ecualizada + Contraste', contrasted)

    # 5. Calcular gradientes Sobel en X y Y
    sobelx = cv2.Sobel(contrasted, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(contrasted, cv2.CV_64F, 0, 1, ksize=5)

    # 6. Convertir los resultados a 8 bits para visualización
    sobelx_abs = cv2.convertScaleAbs(sobelx)
    sobely_abs = cv2.convertScaleAbs(sobely)

    # 7. Mostrar Sobel X e Y
    cv2.imshow('Sobel X', sobelx_abs)
    cv2.imshow('Sobel Y', sobely_abs)

    # 8. Umbralizar con valor manual ajustable
    _, sobelx_bin = cv2.threshold(sobelx_abs, umbral_sobel, 255, cv2.THRESH_BINARY)
    _, sobely_bin = cv2.threshold(sobely_abs, umbral_sobel, 255, cv2.THRESH_BINARY)

    # 9. Operación lógica NAND (NOT del AND)
    and_result = cv2.bitwise_and(sobelx_bin, sobely_bin)
    nand_result = cv2.bitwise_not(and_result)

    # 10. Mostrar el resultado de la operación NAND
    cv2.imshow('NAND (SobelX NAND SobelY)', nand_result)

    # 11. Salir con tecla ESC
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()

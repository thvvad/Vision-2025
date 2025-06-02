# Detección de bordes con ajuste manual de contraste, umbral de Sobel y limpieza morfológica
# Por Vanessa Aguirre

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Parámetros ajustables
contraste_manual = 1       # Aumenta o disminuye el contraste (1 = sin cambio)
umbral_sobel = 250         # Umbral para binarizar Sobel X y Y
kernel_morfologico = 1     # Tamaño del kernel para apertura y cierre (debe ser impar y >1)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # 1. Mostrar imagen original
    cv2.imshow('Original', frame)

    # 2. Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gris', gray)

    # 3. Ecualizar histograma para aumentar contraste general
    equalized = cv2.equalizeHist(gray)

    # 4. Aplicar aumento de contraste manual
    contrasted = cv2.convertScaleAbs(equalized, alpha=contraste_manual, beta=0)
    cv2.imshow('Ecualizada + Contraste', contrasted)

    # 5. Calcular gradientes Sobel X y Y
    sobelx = cv2.Sobel(contrasted, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(contrasted, cv2.CV_64F, 0, 1, ksize=5)

    # 6. Convertir a 8 bits
    sobelx_abs = cv2.convertScaleAbs(sobelx)
    sobely_abs = cv2.convertScaleAbs(sobely)

    # 7. Mostrar Sobel X y Y
    cv2.imshow('Sobel X', sobelx_abs)
    cv2.imshow('Sobel Y', sobely_abs)

    # 8. Umbralización
    _, sobelx_bin = cv2.threshold(sobelx_abs, umbral_sobel, 255, cv2.THRESH_BINARY)
    _, sobely_bin = cv2.threshold(sobely_abs, umbral_sobel, 255, cv2.THRESH_BINARY)

    # 9. NAND lógico: NOT(AND)
    and_result = cv2.bitwise_and(sobelx_bin, sobely_bin)
    nand_result = cv2.bitwise_not(and_result)

    # 10. Crear kernel para operaciones morfológicas
    kernel = np.ones((kernel_morfologico, kernel_morfologico), np.uint8)

    # 11. Aplicar apertura (quita ruido blanco pequeño) y luego cierre (quita puntos negros)
    apertura = cv2.morphologyEx(nand_result, cv2.MORPH_OPEN, kernel)
    cierre = cv2.morphologyEx(apertura, cv2.MORPH_CLOSE, kernel)

    # 12. Mostrar resultado final sin ruido
    cv2.imshow('NAND + Limpieza Morfológica', cierre)

    # 13. Salir con ESC
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Liberar cámara y cerrar ventanas
cap.release()
cv2.destroyAllWindows()

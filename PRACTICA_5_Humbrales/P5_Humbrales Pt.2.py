import numpy as np                 # Librería para manejo de arreglos y matrices
import matplotlib.pyplot as plt   # Para mostrar imágenes gráficamente
import cv2                        # OpenCV: procesamiento de imágenes

# ---------------------------------------
# 1. Cargar imagen y convertir a escala de grises
# ---------------------------------------
img = cv2.imread('bookpage.jpg')                       # Cargar imagen en color
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)           # Convertir a escala de grises

# ---------------------------------------
# 2. Definir parámetros para umbrales fijos
# ---------------------------------------
thresh_val = 127    # Umbral manual
max_val = 255       # Valor máximo (blanco)

# ---------------------------------------
# 3. Aplicar técnicas de umbral fijo
# ---------------------------------------

# Threshold1: THRESH_BINARY
_, binary = cv2.threshold(gray, thresh_val, max_val, cv2.THRESH_BINARY)
# Si el valor del píxel ≥ 127 → se convierte en 255, si no → se convierte en 0 (blanco y negro)

# THRESH_BINARY_INV
_, binary_inv = cv2.threshold(gray, thresh_val, max_val, cv2.THRESH_BINARY_INV)
# Igual que el anterior pero invertido: lo que era blanco ahora es negro, y viceversa

# THRESH_TRUNC
_, trunc = cv2.threshold(gray, thresh_val, max_val, cv2.THRESH_TRUNC)
# Si el valor del píxel > 127 → se convierte en 127, si no → se queda igual

# THRESH_TOZERO
_, tozero = cv2.threshold(gray, thresh_val, max_val, cv2.THRESH_TOZERO)
# Si el valor del píxel < 127 → se convierte en 0, si no → se mantiene

# THRESH_TOZERO_INV
_, tozero_inv = cv2.threshold(gray, thresh_val, max_val, cv2.THRESH_TOZERO_INV)
# Si el valor del píxel > 127 → se convierte en 0, si no → se mantiene

# ---------------------------------------
# 4. Aplicar umbrales adaptativos y Otsu
# ---------------------------------------

# ADAPTIVE_THRESH_MEAN_C (Mean)
mean = cv2.adaptiveThreshold(
    gray, max_val, cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY, 11, 2)
# Calcula el umbral para cada bloque 11x11 como el promedio de sus vecinos menos 2

# ADAPTIVE_THRESH_GAUSSIAN_C (Gaus)
gaus = cv2.adaptiveThreshold(
    gray, max_val, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, 11, 2)
# Similar al anterior pero con una media ponderada gaussiana (valores del centro pesan más)

# THRESH_OTSU
otsu_val, otsu = cv2.threshold(
    gray, 0, max_val, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# Encuentra automáticamente el mejor valor de umbral para separar fondo y objetos


# ---------------------------------------
# 5. Mostrar resultados - Ventana 1 (umbrales fijos)
# ---------------------------------------
plt.figure("Umbrales Fijos", figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.imshow(binary, cmap='gray')
plt.title("THRESH_BINARY")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(binary_inv, cmap='gray')
plt.title("THRESH_BINARY_INV")
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(trunc, cmap='gray')
plt.title("THRESH_TRUNC")
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(tozero, cmap='gray')
plt.title("THRESH_TOZERO")
plt.axis('off')

# ---------------------------------------
# 6. Mostrar resultados - Ventana 2 (adaptativos y Otsu)
# ---------------------------------------
plt.figure("Adaptativos y Otsu", figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.imshow(tozero_inv, cmap='gray')
plt.title("THRESH_TOZERO_INV")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(mean, cmap='gray')
plt.title("ADAPTIVE_THRESH_MEAN_C")
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(gaus, cmap='gray')
plt.title("ADAPTIVE_THRESH_GAUSSIAN_C")
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(otsu, cmap='gray')
plt.title(f"THRESH_OTSU (T={otsu_val:.0f})")  # Mostrar valor calculado por Otsu
plt.axis('off')

# ---------------------------------------
# 7. Mostrar todas las figuras
# ---------------------------------------
plt.tight_layout()
plt.show()



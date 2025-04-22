#Practica 3 Pt.2: Ecualizacion del histograma
# La ecualización de histograma solo puede AUMENTAR el contraste, nunca reducirlo.

import cv2  # OpenCV para procesamiento de imágenes
import matplotlib.pyplot as plt  # Matplotlib para mostrar imágenes y gráficos

# Cargar imagen en color
img_color = cv2.imread('flores.jpg')

# Convertir a escala de grises
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# Aplicar ecualización de histograma
img_eq = cv2.equalizeHist(img_gray)

# Crear una figura para mostrar las imágenes
plt.figure(figsize=(15, 6))

# Mostrar imagen original en color (convertida de BGR a RGB para que se vea bien con matplotlib)
plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB))
plt.title('Original (Color)')
plt.axis('off')  # Quitar ejes

# Mostrar imagen en escala de grises
plt.subplot(2, 3, 2)
plt.imshow(img_gray, cmap='gray')
plt.title('Escala de grises')
plt.axis('off')

# Mostrar imagen ecualizada
plt.subplot(2, 3, 3)
plt.imshow(img_eq, cmap='gray')
plt.title('Ecualizada')
plt.axis('off')

# Histograma de la imagen en escala de grises original
plt.subplot(2, 3, 5)
plt.hist(img_gray.ravel(), 256, [0, 256], color='gray')
plt.title('Histograma - Original')
plt.xlabel('Valor de intensidad')
plt.ylabel('Número de píxeles')

# Histograma de la imagen ecualizada
plt.subplot(2, 3, 6)
plt.hist(img_eq.ravel(), 256, [0, 256], color='black')
plt.title('Histograma - Ecualizada')
plt.xlabel('Valor de intensidad')
plt.ylabel('Número de píxeles')

# Ajustar distribución de los subplots
plt.tight_layout()
plt.show()

# Esperar a que el usuario presione una tecla
cv2.waitKey(0)

# Cerrar todas las ventanas abiertas
cv2.destroyAllWindows()

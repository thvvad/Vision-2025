# Practica 3: Histograma de una imagen

# Importar librerías necesarias
import cv2  # OpenCV: para procesamiento de imágenes
import matplotlib.pyplot as plt  # Matplotlib: para graficar el histograma

# Cargar la imagen a color (por defecto en formato BGR)
img1 = cv2.imread('tata.jpg')  # Cambia 'tata.jpg' por el nombre o ruta de tu imagen

# Cargar la misma imagen en escala de grises
img2 = cv2.imread('tata.jpg', cv2.IMREAD_GRAYSCALE)

# Mostrar la imagen a color en una ventana llamada 'Imagen 1'
cv2.imshow('Imagen 1', img1)

# Mostrar la imagen en escala de grises en una ventana llamada 'Imagen 2'
cv2.imshow('Imagen 2', img2)

# Calcular el histograma de la imagen en escala de grises
# [img2] = imagen de entrada
# [0] = canal 0 (único canal en escala de grises)
# None = sin máscara (se analiza toda la imagen)
# [256] = número de bins (niveles de intensidad)
# [0, 256] = rango de valores de intensidad posibles
hist = cv2.calcHist([img2], [0], None, [256], [0, 256])

# Graficar el histograma con Matplotlib
plt.plot(hist)  # Dibuja la curva del histograma
plt.title('Histograma de imagen en escala de grises')  # Título de la gráfica
plt.xlabel('Valor de intensidad (0-255)')  # Etiqueta eje X
plt.ylabel('Número de píxeles')  # Etiqueta eje Y
plt.grid(True)  # Mostrar cuadrícula
plt.show()  # Mostrar la gráfica en pantalla

# Esperar a que el usuario presione una tecla
cv2.waitKey(0)

# Cerrar todas las ventanas abiertas de OpenCV
cv2.destroyAllWindows()


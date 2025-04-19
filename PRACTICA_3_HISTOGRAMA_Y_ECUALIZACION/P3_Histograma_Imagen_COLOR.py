# Practica 3: Histograma de una imagen

# Importar librerias
import cv2                # Importa la biblioteca OpenCV para procesamiento de imágenes
import matplotlib.pyplot as plt  # Importa Matplotlib para graficar los histogramas

# Cargar la imagen en color (por defecto, OpenCV la carga en formato BGR)
imagen = cv2.imread('tata.jpg')  # Sustituye 'imagen.jpg' por el nombre o ruta de tu imagen

# Definir los canales de color: azul (b), verde (g), rojo (r)
canales = ('b', 'g', 'r')  # Estos son los índices de los canales en OpenCV (BGR)

# Diccionario que relaciona cada canal con su color en la gráfica
colores = {'b':'blue', 'g':'green', 'r':'red'}

# Crear una figura para mostrar los histogramas
plt.figure(figsize=(10,5))  # Define el tamaño de la figura (ancho x alto)

# Iterar sobre cada canal de color
for i, canal in enumerate(canales):
    # Calcular el histograma del canal actual
    # [imagen]     → la imagen de entrada
    # [i]          → el índice del canal (0 para B, 1 para G, 2 para R)
    # None         → no se usa máscara (se analiza toda la imagen)
    # [256]        → número de bins (uno para cada valor de intensidad 0-255)
    # [0, 256]     → rango de valores posibles de intensidad
    hist = cv2.calcHist([imagen], [i], None, [256], [0,256])
    
    # Dibujar el histograma en el gráfico, con su color correspondiente
    plt.plot(hist, color=colores[canal], label=f'Canal {canal.upper()}')
    
    # Limitar el eje X del gráfico de 0 a 256 (niveles de intensidad)
    plt.xlim([0,256])

# Añadir título y etiquetas
plt.title('Histogramas por canal de color')         # Título del gráfico
plt.xlabel('Valor de intensidad (0-255)')           # Eje X: nivel de brillo o color
plt.ylabel('Número de píxeles')                     # Eje Y: cuántos píxeles tienen ese valor
plt.legend()                                        # Mostrar leyenda con nombres de canales
plt.grid(True)                                      # Mostrar una cuadrícula de fondo

cv2.imshow('Imagen',imagen)             # Mostrar la imagen
plt.show()# Mostrar el gráfico

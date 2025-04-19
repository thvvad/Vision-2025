# Practica 3: Histograma de una imagen

# Importar librerías
import cv2  # OpenCV para procesamiento de imágenes
import matplotlib.pyplot as plt  # Matplotlib para mostrar imágenes y graficar histogramas

# Cargar la imagen en color (OpenCV la carga en formato BGR por defecto)
imagen = cv2.imread('tata.jpg')  # Cambia 'tata.jpg' por la ruta o nombre de tu imagen

# Convertir la imagen de BGR a RGB (para que se vea correctamente con matplotlib)
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

# Definir los canales de color: azul (b), verde (g), rojo (r)
canales = ('b', 'g', 'r')  # BGR: Blue, Green, Red en OpenCV

# Diccionario que relaciona cada canal con su color para graficar
colores = {'b': 'blue', 'g': 'green', 'r': 'red'}

# Crear una figura para mostrar la imagen y los histogramas
plt.figure(figsize=(12, 5))  # Tamaño de la figura (ancho x alto en pulgadas)

# Mostrar la imagen original en color (convertida a RGB)
plt.subplot(1, 2, 1)  # 1 fila, 2 columnas, posición 1
plt.imshow(imagen_rgb)
plt.title('Imagen original (RGB)')
plt.axis('off')  # Ocultar ejes

# Crear el segundo subplot para los histogramas
plt.subplot(1, 2, 2)  # Posición 2

# Iterar sobre cada canal y graficar su histograma
for i, canal in enumerate(canales):
    # Calcular el histograma del canal actual
    hist = cv2.calcHist([imagen], [i], None, [256], [0, 256])
    
    # Dibujar el histograma con el color correspondiente
    plt.plot(hist, color=colores[canal], label=f'Canal {canal.upper()}')

# Configurar gráfico
plt.title('Histogramas por canal de color')
plt.xlabel('Valor de intensidad (0-255)')
plt.ylabel('Número de píxeles')
plt.xlim([0, 256])  # Límite del eje X
plt.legend()  # Mostrar leyenda
plt.grid(True)  # Mostrar cuadrícula de fondo

# Ajustar el diseño y mostrar todo
plt.tight_layout()
plt.show()


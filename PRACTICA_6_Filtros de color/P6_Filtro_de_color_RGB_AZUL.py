import cv2                        # Importa la librería OpenCV para visión por computadora
import numpy as np               # Importa la librería NumPy para manejar arreglos numéricos
import matplotlib.pyplot as plt  # Importa matplotlib para mostrar imágenes en un subplot

# Inicia la captura de video desde la cámara principal (índice 0)
cap = cv2.VideoCapture(0)

# Define el rango mínimo y máximo del color azul en formato RGB
min_RGB = np.array([0, 0, 150])         # Azul oscuro (R: bajo, G: bajo, B: alto)
max_RGB = np.array([150, 150, 255])     # Azul claro

# Invierte los valores RGB a BGR porque OpenCV trabaja con BGR
bgr_min = min_RGB[::-1]
bgr_max = max_RGB[::-1]

# Función para crear una barra de degradado del color entre el mínimo y máximo
def create_color_bar(min_color, max_color, width=300, height=50):
    bar = np.zeros((height, width, 3), dtype=np.uint8)  # Crea una imagen negra
    for i in range(width):                              # Para cada columna de la imagen
        alpha = i / width                               # Calcula una proporción para interpolar
        color = (1 - alpha) * min_color + alpha * max_color  # Mezcla entre min y max
        bar[:, i] = color                               # Asigna ese color a la columna
    return bar                                          # Devuelve la imagen de la barra

# Crea la barra de color inicial
color_bar = create_color_bar(bgr_min, bgr_max)

# Variables para almacenar capturas
frame_snap = None
mask_snap = None
res_snap = None
bar_snap = None

# ----------- Bucle principal para captura en vivo ------------------
while True:
    ret, frame = cap.read()                     # Captura un frame desde la cámara
    if not ret:                                 # Si no se pudo capturar correctamente
        break                                   # Sale del bucle

    mask = cv2.inRange(frame, bgr_min, bgr_max)       # Crea una máscara del color azul
    res = cv2.bitwise_and(frame, frame, mask=mask)    # Aplica la máscara para mostrar solo el azul

    cv2.imshow('frame', frame)                 # Muestra la imagen original
    cv2.imshow('mask', mask)                   # Muestra la máscara (blanco donde hay azul)
    cv2.imshow('res', res)                     # Muestra el resultado de aplicar la máscara
    cv2.imshow('Color Range (RGB)', color_bar) # Muestra la barra del rango de color azul

    key = cv2.waitKey(5) & 0xFF                # Espera por una tecla durante 5 ms

    if key == 27:                              # Si se presiona ESC (código 27), sale del bucle
        break

    elif key == 32:                            # Si se presiona espacio (código 32)
        frame_snap = frame.copy()              # Guarda una copia del frame original
        mask_snap = mask.copy()                # Guarda una copia de la máscara
        res_snap = res.copy()                  # Guarda una copia del resultado
        bar_snap = color_bar.copy()            # Guarda una copia de la barra de color

        # Cambia el espacio de color de BGR a RGB para mostrarlo con matplotlib
        frame_rgb = cv2.cvtColor(frame_snap, cv2.COLOR_BGR2RGB)
        res_rgb = cv2.cvtColor(res_snap, cv2.COLOR_BGR2RGB)
        bar_rgb = cv2.cvtColor(bar_snap, cv2.COLOR_BGR2RGB)

        # Crea una figura con subplots
        plt.figure(figsize=(10, 6))  # Define el tamaño de la figura

        # Imagen original
        plt.subplot(2, 2, 1)         # Primer subplot
        plt.imshow(frame_rgb)       # Muestra la imagen original convertida a RGB
        plt.title('Original')       # Título del subplot
        plt.axis('off')             # Oculta los ejes

        # Máscara binaria
        plt.subplot(2, 2, 2)
        plt.imshow(mask_snap, cmap='gray')   # Muestra la máscara en escala de grises
        plt.title('Mask')
        plt.axis('off')

        # Resultado del filtro
        plt.subplot(2, 2, 3)
        plt.imshow(res_rgb)         # Muestra el resultado en RGB
        plt.title('Filtered Result')
        plt.axis('off')

        # Barra de color
        plt.subplot(2, 2, 4)
        plt.imshow(bar_rgb)         # Muestra la barra de color
        plt.title('Color Range Bar')
        plt.axis('off')

        plt.tight_layout()          # Ajusta el espaciado entre subplots
        plt.show()                  # Muestra la figura

# Libera la cámara
cap.release()

# Cierra todas las ventanas de OpenCV
cv2.destroyAllWindows()

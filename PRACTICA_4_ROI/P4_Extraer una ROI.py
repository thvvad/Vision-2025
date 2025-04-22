# Practica 4:Extraer una ROI rectangular (Region de interes)

#Importar libreria
import cv2

# Cargar la imagen desde archivo
imagen = cv2.imread('v2.jpeg')

# Coordenadas de la esquina superior izquierda de la ROI
x = 100  # posición en x
y = 150   # posición en y

# Tamaño de la ROI (ancho y alto)
w = 200  # ancho de la ROI
h = 250  # alto de la ROI

# Dibujar un rectángulo verde sobre la imagen para mostrar la ROI
cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Extraer la ROI de la imagen (recordar que la imagen se indexa como [fila, columna])
roi = imagen[y:y + h, x:x + w]

# Mostrar la imagen original con el rectángulo de la ROI
cv2.imshow("Imagen original con ROI", imagen)

# Mostrar la ROI extraída por separado
cv2.imshow("ROI extraída", roi)

# Esperar a que el usuario presione una tecla
cv2.waitKey(0)

# Cerrar todas las ventanas abiertas
cv2.destroyAllWindows()

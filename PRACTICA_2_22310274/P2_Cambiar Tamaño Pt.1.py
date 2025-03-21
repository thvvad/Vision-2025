# Practica 2: Operaciones Aritmeticas... Redimencionar una imagen
# Vanessa Aguirre Diaz

# Importar librerias:
import cv2

# Cargar imagen
img = cv2.imread('tata.jpg')

# Factores de escala (50% del tamaño original)
escala_x = 0.4  # Reducir el ancho al 50%
escala_y = 0.4  # Reducir el alto al 50%

# Redimensionar con factores de escala
img_reducida = cv2.resize(img, None, fx=escala_x, fy=escala_y, interpolation=cv2.INTER_LINEAR)

# Redimensionar a un tamaño específico (ancho=300, alto=200)
img_redimensionada = cv2.resize(img, (300, 200))

# Mostrar imagen original y redimensionada
cv2.imshow('Imagen Original', img)
cv2.imshow('Imagen Reducida', img_reducida)
cv2.imshow('Imagen Redimensionada', img_redimensionada)

cv2.waitKey(0)                  # Esperar a que el usuario presione una tecla para cerrar la ventana
cv2.destroyAllWindows()         # Cerrar todas las ventanas de OpenCV.

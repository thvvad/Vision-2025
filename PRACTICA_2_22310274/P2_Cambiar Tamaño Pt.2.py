# Practica 2: Operaciones Aritmeticas... Redimencionar una imagen
# Vanessa Aguirre Diaz

# Importar librerias:
import cv2

# Cargar imagen
img = cv2.imread('chimmy.jpg')

# Obtener dimensiones originales
alto, ancho = img.shape[:2]

# Nuevo tamaño manteniendo la relación de aspecto (reducir a 50%)
factor1 = 0.5
factor2 = 1.5

nuevo_ancho1 = int(ancho * factor1)
nuevo_alto1 = int(alto * factor1)

nuevo_ancho2 = int(ancho * factor2)
nuevo_alto2 = int(alto * factor2)

# Redimensionar
img_reducida = cv2.resize(img, (nuevo_ancho1, nuevo_alto1), interpolation=cv2.INTER_AREA)
img_aumentada = cv2.resize(img, (nuevo_ancho2, nuevo_alto2), interpolation=cv2.INTER_AREA)

# Mostrar imágenes
cv2.imshow('Original', img)
cv2.imshow('Reducida', img_reducida)
cv2.imshow('Aumentada', img_aumentada)

cv2.waitKey(0)                  # Esperar a que el usuario presione una tecla para cerrar la ventana
cv2.destroyAllWindows()         # Cerrar todas las ventanas de OpenCV.

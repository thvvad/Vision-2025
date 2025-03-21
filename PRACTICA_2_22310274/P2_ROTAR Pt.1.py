# Practica 2: Operaciones Aritmeticas... Rotar una imagen
# Vanessa Aguirre Diaz

# Importar librerias:
import cv2

# Cargar imagen
img = cv2.imread('tata.jpg')

# Rotar 90° en sentido horario
rotada_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Rotar 90° en sentido antihorario
rotada_90_anti = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Rotar 180°
rotada_180 = cv2.rotate(img, cv2.ROTATE_180)

# Mostrar imágenes
cv2.imshow('Original', img)
cv2.imshow('Rotada 90° Horario', rotada_90)
cv2.imshow('Rotada 90° Antihorario', rotada_90_anti)
cv2.imshow('Rotada 180°', rotada_180)

cv2.waitKey(0)                  # Esperar a que el usuario presione una tecla para cerrar la ventana
cv2.destroyAllWindows()         # Cerrar todas las ventanas de OpenCV.

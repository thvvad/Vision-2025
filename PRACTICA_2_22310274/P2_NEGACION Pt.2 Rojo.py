# Practica 2: Operaciones Aritmeticas... Negacion de un solo color
# Vanessa Aguirre Diaz

# Importar librerias:
import cv2

# Cargar imagen
img = cv2.imread('tata.jpg')

# Separar canales BGR
b, g, r = cv2.split(img)

# Negar solo el canal rojo
r_negado = cv2.bitwise_not(r)

# Negar solo el canal azul
b_negado = cv2.bitwise_not(b)

# Negar solo el canal verde
g_negado = cv2.bitwise_not(g)

# Fusionar de nuevo los canales
rojo_negado = cv2.merge([b, g, r_negado])
azul_negado = cv2.merge([b_negado, g, r])
verde_negado = cv2.merge([b, g_negado, r])

# Mostrar imágenes
cv2.imshow('Original', img)
cv2.imshow('Rojo Negado', rojo_negado)
cv2.imshow('Azul Negado', azul_negado)
cv2.imshow('Verde Negado', verde_negado)

cv2.waitKey(0)                  # Esperar a que el usuario presione una tecla para cerrar la ventana
cv2.destroyAllWindows()         # Cerrar todas las ventanas de OpenCV.

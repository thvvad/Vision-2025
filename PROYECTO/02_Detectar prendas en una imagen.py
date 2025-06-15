# Importa la librería OpenCV para procesamiento de imágenes
import cv2

# Lee la imagen desde archivo
imagen = cv2.imread('vestb.jpg')  # Cambia 'ropa.jpg' por el nombre de tu imagen

# Redimensiona la imagen para que no sea tan grande (opcional)
imagen = cv2.resize(imagen, (640, 480))

# Convierte la imagen original a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplica un desenfoque para reducir ruido y mejorar la detección
gris_suavizado = cv2.GaussianBlur(gris, (5, 5), 0)

# Aplica una umbralización para segmentar los objetos (blanco sobre negro)
_, umbral = cv2.threshold(gris_suavizado, 60, 255, cv2.THRESH_BINARY_INV)

# Encuentra los contornos (bordes cerrados) en la imagen umbralizada
contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Recorre todos los contornos detectados
for contorno in contornos:
    # Calcula el área del contorno
    area = cv2.contourArea(contorno)

    # Filtra contornos muy pequeños (ruido)
    if area > 500:
        # Calcula un rectángulo que encierra el contorno
        x, y, w, h = cv2.boundingRect(contorno)

        # Dibuja el rectángulo en la imagen original (color verde)
        cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Muestra la imagen con los rectángulos detectados
cv2.imshow('Prendas detectadas', imagen)

# Espera a que el usuario presione una tecla para cerrar la ventana
cv2.waitKey(0)

# Cierra todas las ventanas abiertas por OpenCV
cv2.destroyAllWindows()

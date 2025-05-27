import cv2  # Importa la librería OpenCV para visión artificial
import numpy as np  # Importa NumPy para manejar matrices

# Inicia la captura de video desde la cámara (0 = cámara por defecto)
cap = cv2.VideoCapture(0)

# Bucle principal para capturar video en tiempo real
while True:
    ret, frame = cap.read()  # Lee un frame (imagen) de la cámara

    # Convierte la imagen de BGR (formato por defecto) a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define el rango inferior y superior del color a detectar en formato HSV
    # Puedes ajustar estos valores según el color que desees filtrar
    lower = np.array([30, 150, 50])     # Límite inferior del color
    upper = np.array([255, 255, 180])   # Límite superior del color

    # Crea una máscara binaria: blanco donde el color está dentro del rango, negro donde no
    mask = cv2.inRange(hsv, lower, upper)

    # Crea un kernel (estructura) de 5x5 píxeles para aplicar operaciones morfológicas
    kernel = np.ones((5, 5), np.uint8)

    # Aplica una apertura (erosión seguida de dilatación)
    # Esto elimina pequeños puntos blancos (ruido) en la máscara
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Aplica un cierre (dilatación seguida de erosión)
    # Esto rellena pequeños agujeros negros dentro de objetos blancos detectados
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    # Aplica la máscara ya limpia a la imagen original, dejando solo la parte detectada
    result = cv2.bitwise_and(frame, frame, mask=closing)

    # Muestra las diferentes ventanas: imagen original, máscara limpia y resultado final
    cv2.imshow('Original', frame)        # Imagen original capturada por la cámara
    cv2.imshow('Filtrado', closing)      # Máscara después de limpiar el ruido
    cv2.imshow('Resultado', result)      # Resultado aplicando la máscara a la imagen

    # Espera 5 ms por una tecla. Si es 'ESC' (código 27), se rompe el bucle
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Libera la cámara y cierra todas las ventanas abiertas
cap.release()
cv2.destroyAllWindows()

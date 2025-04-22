#Practica 4: Seleccion manual de una ROI
import cv2

# Cargar imagen
imagen = cv2.imread('v2.jpeg')

# --- Paso 1: Mostrar ventana para seleccionar ROI manualmente ---
# selectROI devuelve (x, y, w, h)
roi = cv2.selectROI("Selecciona una ROI con el mouse", imagen, fromCenter=False, showCrosshair=True)

# Destruir la ventana de selección después de usarla
cv2.destroyWindow("Selecciona una ROI con el mouse")

# --- Paso 2: Extraer la ROI usando slicing ---
x, y, w, h = roi
roi_extraida = imagen[y:y+h, x:x+w]

# --- Paso 3: Mostrar la imagen original y la ROI por separado ---
cv2.imshow("Imagen original", imagen)
cv2.imshow("ROI seleccionada", roi_extraida)

# Esperar hasta que se presione una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()

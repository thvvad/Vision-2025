# Práctica 2: Operaciones
# Por Vanessa Aguirre Diaz

import numpy as np
import cv2

cap = cv2.VideoCapture(0)  # Esto devolverá el video de la primera cámara web de tu computadora
 
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



# Notas:
# 1. OpenCV lee los colores como BGR (azul, verde, rojo), mientras que la mayoría de las aplicaciones informáticas los leen como RGB (rojo, verde, azul).

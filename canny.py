#Biblioteca
import cv2
#Capturar informacion
capture = cv2.VideoCapture(0)

while capture.isOpened():
    ret, frame = capture.read()

    if ret:
        # Aplicar Canny
        borderCanny = cv2.Canny(frame, 100, 200)

        # Mostrar imágenes
        cv2.imshow('original', frame)
        cv2.imshow('blur', borderCanny)

        # Presionar una tecla para dejar de ejecutar
        if cv2.waitKey(1) == ord('s'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()


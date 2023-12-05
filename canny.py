#Bibliotecas
import cv2
#Abrir Imagenes
img = cv2.imread('libro.jpg', 0)
borderCanny = cv2.Canny(img, 100, 200)
#Mostrar imagenes
cv2.imshow('original', img)
cv2.imshow('blur', borderCanny)
#Presionar una tecla para dejar de ejecutar
cv2.waitKey(0)
cv2.destroyAllWindows()


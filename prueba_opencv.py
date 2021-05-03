import cv2
import numpy as numpy

img = cv2.imread("FF7.jpg")
cv2.imshow("Original image", img)
#edge_img = cv2.Canny(img,100,200)
#cv2.imshow("edge", edge_img)

color_bajo = (20,39,56)
color_alto = (200,200,200)

imagen_salida = img.copy()
imagen_salida_rgb = cv2.cvtColor(imagen_salida, cv2.COLOR_BGR2RGB)
imagen_salida_hsv = cv2.cvtColor(imagen_salida, cv2.COLOR_BGR2HSV)
mascara = cv2.inRange(imagen_salida_hsv, color_bajo, color_alto)
resultado = cv2.bitwise_and(imagen_salida, imagen_salida_hsv, mask=mascara)


cv2.imshow("Mostrar Imagen OPENCV",resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()
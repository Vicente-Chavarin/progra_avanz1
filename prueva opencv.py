import cv2
import numpy as np

img = cv2.imread("FF7.jpg")

cv2.imshow("Mostrar Imagen OPENCV",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
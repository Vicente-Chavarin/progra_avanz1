import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("captura.png")
#
#min = [1, 0, 20]
#max = [60, 40, 200]
#min = np.array(min, dtype="uint8")
#max = np.array(max, dtype="uint8")
#mask = cv2.inRange(img, min, max)
#
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cuadro = cv2.rectangle (gris,(150, 150), (350,350), (0, 255, 0), 2)
ret, thresh = cv2.threshold(gris, 127, 255,0)
contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(255,0,0),2)
cv2.imshow("captura.png",img)
cv2.waitKey()
cv2.destroyAllWindows()
#plt.imshow(gris)
#plt.show()


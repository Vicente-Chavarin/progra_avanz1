import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("captura.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cuadro = cv2.rectangle (img,(150, 150), (350,350), (0,0,255), 2)
    #cv2.imshow("imagen en gris", gris)
    #cv2.waitKey()
    #cv2.destroyAllWindows()
_,binaria = cv2.threshold(gris,127,255,cv2.THRESH_BINARY)
np.array(gris)
plt.imshow(binaria, cmap="gray")
plt.show()
#ret, thresh = cv2.threshold(gris, 127, 255, 0)
contours,_ = cv2.findContours(binaria, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(img,contours,-1,(0,255,0),2)
#cv2.imshow("captura.png",img)
#cv2.waitKey()
#cv2.destroyAllWindows()
plt.imshow(img)
plt.show()
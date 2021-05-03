import cv2
import numpy as np
img = cv2.imread("Circulos.jpg")
output = img.copy()

salida = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(salida, cv2.HOUGH_GRADIENT, 1,30,param1=40,param2=21,minRadius=20,maxRadius=40)
#circles = cv2.HoughCircles(salida, cv2.HOUGH_GRADIENT, 3,30,param1=80,param2=20)
#circlesMax = cv2.HoughCircles(salida, cv2.HOUGH_GRADIENT, 3,30,param1=80,param2=20,minRadius=20,maxRadius=40)
circlesMax = cv2.HoughCircles(salida, cv2.HOUGH_GRADIENT, 1,30,param1=80,param2=20,minRadius=30,maxRadius=60)
circlesMin = cv2.HoughCircles(salida, cv2.HOUGH_GRADIENT, 1,30,param1=20,param2=10,minRadius=10,maxRadius=20)

img = img.astype(np.int32)

circles = np.int32(np.around(circles))
circlesMax = np.int32(np.around(circlesMax))
circlesMin = np.int32(np.around(circlesMin))

for r in circlesMax[0,:]:
    #Rojo
    cv2.circle(img,(r[0],r[1]),r[2],(0,0,255),2)
for v in circlesMin[0,:]:
    #Verde
    cv2.circle(img,(v[0],v[1]),v[2],(0,255,0),2)
for i in circles[0,:]:
    #Negro
    cv2.circle(img,(i[0],i[1]),i[2],(0,0,0),2)
cv2.imshow("Circle",img)
cv2.waitKey()
cv2.destroyAllWindows()
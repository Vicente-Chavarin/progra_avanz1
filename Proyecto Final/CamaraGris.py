from cv2 import *
import numpy as np
import matplotlib.pyplot as plt

namedWindow("webcam")
vc = VideoCapture(0);

while True:
    next, frame = vc.read()
    #Cuando se deja presionado la tecla W la camara se activara, si se deja de pulsar esta se detendra con la ultima iagen que se detecte
    if waitKey(2) == ord("w"):
        cv2.rectangle (frame,(150, 150), (350,350), (0, 255, 0), 2)
        cv2.imshow("webcam", frame)
        img = cv2.imread("webcam")
        _,binaria = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
        contours,_ = cv2.findContours(binaria, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        img = cv2.drawContours(img,contours,-1,(0,255,0),2)
    if waitKey(3) == ord("c"):
        cv2.imshow(img,frame)
        cv2.waitKey()
        cv2.destroyAllWindows()
    #Cuando se presion Q la camara se apaga y finaliza el programa
    if waitKey(1) == ord("q"):
        break;
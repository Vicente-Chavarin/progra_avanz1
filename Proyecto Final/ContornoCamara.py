from cv2 import *

#import numpy as np

namedWindow("webcam")
vc = VideoCapture(0);

while True:
    next, frame = vc.read()
    #Cuando se deja presionado la tecla W la camara se activara, si se deja de pulsar esta se detendra con la ultima iagen que se detecte
    if waitKey(2) == ord("w"):
        cv2.imshow("webcam", frame);
    #Cuando se presiona la tecla e se tomara una captura del ultimo frame.
    if waitKey(3) == ord("e"):
        cv2.imwrite("Captura.png", frame);
        print("Foto tomada correctamente")
    #Cuando se presiona la tecla C se muestra la captura tomada con aterioridad
    if waitKey(4) == ord("c"):
        cv2.imshow("captura.png",frame);
    #Cuando se presiona la tecla A se muestra el controno de la imagen camputrada
    #if waitKey(5) == ord("a"):
      #  img = cv2.imread("captura.png")
       # color = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
       # contorno = cv2.threshold(color,0,0,255)
        #cv2.findContours(contorno,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
       # img = cv2.drawContours(img, contorno)
        #cv2.imshow("captura.png")
    #Cuando se presion Q la camara se apaga y finaliza el programa
    if waitKey(1) == ord("q"):
        break;
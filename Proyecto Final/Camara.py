from cv2 import *

namedWindow("webcam")
vc = VideoCapture(0);

while True:
    next, frame = vc.read()
    #Cuando se deja presionado la tecla W la camara se activara, si se deja de pulsar esta se detendra con la ultima iagen que se detecte
    if waitKey(2) == ord("w"):
        imshow("webcam", frame);
    #if waitKey(3) == ord("e"):
    #Cuando se presion Q la camara se apaga y finaliza el programa
    if waitKey(1) == ord("q"):
        break;
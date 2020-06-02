import numpy as np
import cv2

cap=cv2.VideoCapture(0)

while(cap.isOpened()):
    ret,frame = cap.read()
    thresh1 = cv2.applyColorMap(frame,cv2.COLORMAP_HSV)
    cv2.imshow('frame',thresh1)

    if cv2.waitKey(100)&0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

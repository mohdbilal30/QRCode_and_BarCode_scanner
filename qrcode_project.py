import cv2
import numpy as np
from pyzbar.pyzbar import decode

# img = cv2.imread("qr1.jpg")
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

with open("myDataFile.txt") as f:
    myDataList = f.read().splitlines()

while True:

    success,img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode("utf-8") #converting barcode data to string
        print(myData)

        if myData in myDataList:
            # print("Authorised")
            myOutput = "Authorised"
            myColor = (0,255,0)
        else:
            # print("Unauthorised")
            myOutput = "Unauthorised"
            myColor = (0,0,255)
        
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,myColor,5)
        pts2 = barcode.rect
        cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
        0.6,myColor,2)

    cv2.imshow("Results",img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()



import cv2 as cv
face_cascade=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv.VideoCapture(0,cv.CAP_DSHOW)
while(True):
    ret,frame=cap.read()
    face=face_cascade.detectMultiScale(frame,1.1,3)
    for(x,y,w,h) in face:
        cv.rectangle(frame,(x,y,w,h),(0,0,255),2)
        
    cv.putText(frame,f'FACES:{int(len(face))}',(150,50),cv.FONT_HERSHEY_PLAIN,3,(255,250,250),3)
    cv.imshow("CAMERA ",frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

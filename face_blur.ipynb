# Face Blur code
import cv2

# Provide the full path to the Haar Cascade classifier XML file for face detection
face_cascade = cv2.CascadeClassifier('C:\\Users\\DELL 3800\\Desktop\\DS2021\\haarcascade_frontalface_default.xml')


#opening cam
cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

  
    for (x, y, w, h) in faces:
    
        face = frame[y:y+h, x:x+w]
        blurred = cv2.GaussianBlur(frame, (99, 99), 0)
        frame[y:y+h, x:x+w] = blurred[y:y+h, x:x+w]

   
    cv2.imshow('Face Detection with Blur', frame)

    # ENter to exit from the LOOP
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()

import cv2 #pip install opencv-python
import time
import ctypes


# Load pre-trained Haarcascades for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Set the screen lock duration in seconds
lock_duration = 30

def lock_screen():
    ctypes.windll.user32.LockWorkStation()  # Lock the screen for Windows

cap = cv2.VideoCapture(0)

last_detection_time = time.time()

try:
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        if len(faces) > 0:
            last_detection_time = time.time()  # Update the last detection time
            
        if time.time() - last_detection_time > lock_duration:
            lock_screen()
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()

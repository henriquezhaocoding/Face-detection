import cv2 #pip install opencv-python
import time
import ctypes

# Load pre-trained Haarcascades for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Set the screen lock duration in seconds
lock_duration = 3

# Function to lock the screen
def lock_screen():
    ctypes.windll.user32.LockWorkStation()  # Lock the screen for Windows

# Initialize the camera
cap = cv2.VideoCapture(0)

# Initialize variables
last_detection_time = time.time()

try:
    while True:
        # Capture frame from the camera
        ret, frame = cap.read()

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        # Check if faces are detected
        if len(faces) > 0:
            last_detection_time = time.time()  # Update the last detection time

        # Check if more than lock_duration seconds have passed without detecting a face
        if time.time() - last_detection_time > lock_duration:
            lock_screen()
            break

        # Display the frame
        #cv2.imshow('Camera', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
import cv2

# Replace with your ESP32-CAM IP address
ESP32_CAM_URL = 'http://10.155.203.84/stream'

# Open video stream
cap = cv2.VideoCapture(ESP32_CAM_URL)

if not cap.isOpened():
    print("Error: Could not open video stream")
    exit()

# Desired resolution
width = 1280#1920
height = 720#1080

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Resize frame to 1920x1080
    frame_resized = cv2.resize(frame, (width, height), interpolation=cv2.INTER_LANCZOS4)

    # Display the video
    cv2.imshow('ESP32-CAM 1080p', frame_resized)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
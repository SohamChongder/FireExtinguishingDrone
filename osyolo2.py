import cv2
import ultralytics
from ultralytics import YOLO
import sys
import serial
arduinoData = serial.Serial('/dev/tty.usbmodem11301')

# Initialize YOLO model
model = YOLO('200epo.pt')

# Initialize video capture from the default camera (change the index if using a different camera)
cap = cv2.VideoCapture(0)

fire_detected = False

while True:
    # Read frame from camera
    ret, frame = cap.read()
    
    # Perform object detection
    results = model.predict(frame)
    
    detected = False  # Initialize detection flag
    
    for result in results:
        if len(result.boxes) > 0:  # Check if any boxes are detected
            detected = True  # Set detected to True
            for bbox in result.boxes.xyxy:
                x1, y1, x2, y2 = bbox[0].item(), bbox[1].item(), bbox[2].item(), bbox[3].item()
                centroid = ((x1 + x2) / 2, (y1 + y2) / 2)
                break  # Only consider the first detected box and centroid

    if detected:
        fire_detected = True
        print("Fire Detected")
        print("Centroid:", centroid)
        print("True")
        cmd = "1"
        # break  # Stop the code execution if fire is detected
    if not fire_detected:
        print("No fire detected")
        print("False")
        cmd = "0"
        # break

    # Display frame with bounding boxes and centroid
    cv2.imshow("Fire Detection", frame)
    
    # Check for 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close windows
cap.release()
cv2.destroyAllWindows()
# while True:
#     cmd = cmd+'\r'
#     arduinoData.write(cmd.encode())

# Check if no fire is detected and stop execution


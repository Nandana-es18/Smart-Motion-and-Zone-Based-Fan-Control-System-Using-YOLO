#yolo code (after 5 seconds ON/OFF)
import cv2
import requests
import numpy as np
import time
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# ESP32 IP Address
ESP32_IP = "http://192.168.0.101"  # Change this to your ESP32 IP

# Open video capture
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the Iriun Webcam.")
    exit()

ret, frame = cap.read()
if not ret:
    print("Error: Could not read video frame.")
    exit()

frame_height, frame_width, _ = frame.shape
mid_x, mid_y = frame_width // 2, frame_height // 2

# Track timers and zone states
zone_timers = {"Zone 1": None, "Zone 2": None, "Zone 3": None, "Zone 4": None}
zone_off_timers = {"Zone 1": None, "Zone 2": None, "Zone 3": None, "Zone 4": None}
zone_status = {"Zone 1": 0, "Zone 2": 0, "Zone 3": 0, "Zone 4": 0}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    detected_zones = {"Zone 1": False, "Zone 2": False, "Zone 3": False, "Zone 4": False}

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0]) 
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            class_id = int(box.cls[0])  

            if class_id == 0:
                if cx < mid_x and cy < mid_y:
                    detected_zones["Zone 1"] = True
                elif cx >= mid_x and cy < mid_y:
                    detected_zones["Zone 2"] = True
                elif cx < mid_x and cy >= mid_y:
                    detected_zones["Zone 3"] = True
                else:
                    detected_zones["Zone 4"] = True

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    current_time = time.time()
    
    for zone in zone_timers:
        if detected_zones[zone]:  
            if zone_status[zone] == 0:  # Light is OFF, check if we need to turn it ON
                if zone_timers[zone] is None:  
                    zone_timers[zone] = current_time  # Start ON timer
                elif current_time - zone_timers[zone] >= 5:  # If 5 sec passed
                    try:
                        response = requests.get(f"{ESP32_IP}/control?zone={list(zone_status.keys()).index(zone) + 1}&status=1", timeout=2)
                        print(f"Sent to ESP32: {zone} -> ON | Response: {response.text}")
                        zone_status[zone] = 1  # Mark as ON
                    except requests.exceptions.RequestException as e:
                        print(f"Error sending data to ESP32: {e}")

            # Reset OFF timer since person is present
            zone_off_timers[zone] = None  

        else:  
            if zone_status[zone] == 1:  
                if zone_off_timers[zone] is None:  
                    zone_off_timers[zone] = current_time  
                elif current_time - zone_off_timers[zone] >= 5:  
                    try:
                        response = requests.get(f"{ESP32_IP}/control?zone={list(zone_status.keys()).index(zone) + 1}&status=0", timeout=2)
                        print(f"Sent to ESP32: {zone} -> OFF | Response: {response.text}")
                        zone_status[zone] = 0  
                    except requests.exceptions.RequestException as e:
                        print(f"Error sending data to ESP32: {e}")
                    zone_off_timers[zone] = None  

            # If zone became inactive and then becomes active again, reset ON timer
            if zone_timers[zone] is not None:
                zone_timers[zone] = None  # Reset ON timer for fresh delay when re-entering

    # Draw zone lines
    cv2.line(frame, (mid_x, 0), (mid_x, frame_height), (255, 0, 0), 2)
    cv2.line(frame, (0, mid_y), (frame_width, mid_y), (255, 0, 0), 2)

    # Display zone labels
    for i, zone in enumerate(zone_status.keys(), start=1):
        cv2.putText(frame, f"{zone}: {'Active' if detected_zones[zone] else 'Inactive'}", 
                    (10 if i % 2 == 1 else mid_x + 10, (30 if i < 3 else mid_y + 30)), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("YOLOv8 Zone Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



from flask import Flask, render_template, Response, request, jsonify
import cv2
import requests
import numpy as np
import time
from ultralytics import YOLO
import threading
import queue
import os

app = Flask(__name__)

ESP32_IP = "http://192.168.157.211"
MODEL_PATH = "yolov8n.pt"
CAMERA_INDEX = 0

# Global Variables
auto_mode = False
video_queue = queue.Queue()
model = YOLO(MODEL_PATH)
cap = None
zone_status = {1: 0, 2: 0, 3: 0, 4: 0}  # Store fan status for each zone

@app.route('/')
def index():
    return render_template('index.html', esp32_ip=ESP32_IP)

@app.route('/toggle_mode', methods=['POST'])
def toggle_mode():
    global auto_mode
    data = request.json
    auto_mode = data.get("auto_mode", False)
    
    if auto_mode:
        print("Switched to Auto Mode: Running YOLO Script")
    else:
        print("Switched to Manual Mode: Displaying FAN ON/OFF Controls")
    
    return jsonify({"success": True, "mode": "auto" if auto_mode else "manual"})

@app.route('/fan_control', methods=['POST'])
def fan_control():
    data = request.json
    zone = data.get("zone")
    state = data.get("state")  # 1 for ON, 0 for OFF
    
    if zone not in zone_status:
        return jsonify({"error": "Invalid zone"}), 400
    
    try:
        response = requests.get(f"{ESP32_IP}/control?zone={zone}&status={state}", timeout=2)
        zone_status[zone] = state
        return jsonify({"success": True, "zone": zone, "state": "ON" if state else "OFF"})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"ESP32 request failed: {e}"}), 500

# Video Streaming Route
def generate_frames():
    while True:
        frame = video_queue.get()
        if frame is None:
            break
        ret, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Favicon Error Fix
@app.route('/favicon.ico')
def favicon():
    return '', 204

# YOLO Processing
def yolo_processing_thread():
    global auto_mode, cap

    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        if auto_mode:
            ret, frame = cap.read()
            if not ret:
                break

            results = model(frame)
            detected_zones = {1: False, 2: False, 3: False, 4: False}

            for result in results:
                for box in result.boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                    class_id = int(box.cls[0])

                    if class_id == 0:
                        if cx < frame.shape[1] // 2 and cy < frame.shape[0] // 2:
                            detected_zones[1] = True
                        elif cx >= frame.shape[1] // 2 and cy < frame.shape[0] // 2:
                            detected_zones[2] = True
                        elif cx < frame.shape[1] // 2 and cy >= frame.shape[0] // 2:
                            detected_zones[3] = True
                        else:
                            detected_zones[4] = True

                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            for zone in detected_zones:
                if detected_zones[zone] and zone_status[zone] == 0:
                    try:
                        requests.get(f"{ESP32_IP}/control?zone={zone}&status=1", timeout=2)
                        zone_status[zone] = 1
                    except:
                        pass
                elif not detected_zones[zone] and zone_status[zone] == 1:
                    try:
                        requests.get(f"{ESP32_IP}/control?zone={zone}&status=0", timeout=2)
                        zone_status[zone] = 0
                    except:
                        pass

            video_queue.put(frame)
        else:
            time.sleep(0.1)

yolo_thread = threading.Thread(target=yolo_processing_thread, daemon=True)
yolo_thread.start()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

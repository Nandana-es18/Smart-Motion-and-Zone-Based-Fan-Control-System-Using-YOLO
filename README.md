# Smart Motion and Zone-Based Fan Control System Using YOLOv8

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-lightgrey?style=for-the-badge&logo=flask">
  <img src="https://img.shields.io/badge/YOLOv8-Object%20Detection-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/ESP32-Hardware-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-red?style=for-the-badge">
</p>

---

# Overview

The Smart Motion and Zone-Based Fan Control System is an AI-powered automation framework that combines Computer Vision, Deep Learning, and IoT technologies to automatically control fans based on human presence detection.

The system utilizes YOLOv8 for real-time person detection through a live camera feed and dynamically controls fans across multiple room zones using an ESP32 microcontroller and relay modules.

The primary objectives of the system are:
- Improve energy efficiency
- Reduce unnecessary power consumption
- Enable intelligent environmental control
- Provide real-time monitoring and manual override

---

# Key Features

- Real-time human detection using YOLOv8
- Multi-zone smart fan control architecture
- Automatic fan activation based on occupancy
- Manual control mode through web interface
- Live video streaming with detection overlays
- Automatic fan shutdown after inactivity
- ESP32-based wireless communication
- Energy-efficient smart automation

---

# System Workflow

1. The camera captures a live video stream.
2. YOLOv8 detects people in real time.
3. Detected persons are mapped into predefined zones.
4. Corresponding fans are activated automatically.
5. If no motion is detected for 5 seconds, the fans turn OFF automatically.
6. Users can switch to Manual Mode using the web interface.

---

# System Architecture

## AI Detection Layer
- YOLOv8 object detection
- Real-time person tracking
- Zone mapping logic

## Backend Layer
- Flask-based backend server
- Detection processing
- Fan control communication

## Hardware Layer
- ESP32 microcontroller
- Relay module for fan switching

## Frontend Layer
- Interactive web interface
- Live monitoring dashboard
- Auto and Manual control modes

---

# Project Structure

```bash
SMART-FAN-ZONE-CONTROL/
│
├── demo/                    # Demo videos and reports
├── docs/                    # Documentation
├── templates/               # HTML templates
├── static/                  # CSS, JavaScript, assets
├── ESP32_Code/              # ESP32 microcontroller code
│
├── app.py                   # Flask application
├── backend.py               # YOLOv8 detection and fan control logic
├── frontend.html            # Main frontend interface
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend development |
| Flask | Web framework |
| OpenCV | Video processing |
| YOLOv8 | Human detection |
| ESP32 | Hardware communication |
| HTML/CSS/JS | Frontend development |
| Relay Module | Fan switching |

---

# Working Principle

The system continuously processes live video frames using the YOLOv8 deep learning model.

When a person is detected inside a predefined zone:
- The corresponding fan is activated automatically.
- Detection results are displayed on the web interface with bounding boxes.

If the zone becomes empty:
- A timer starts running.
- The fan turns OFF automatically after 5 seconds of inactivity.

The user can also:
- Enable Manual Mode
- Turn individual fans ON or OFF through the interface

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/SMART-FAN-ZONE-CONTROL.git

cd SMART-FAN-ZONE-CONTROL
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install flask opencv-python ultralytics requests
```

---

# Running the System

## Start Backend Server

```bash
python backend.py
```

or

```bash
python app.py
```

---

## Open Web Interface

```bash
http://127.0.0.1:5000
```

---

# ESP32 Setup

1. Connect ESP32 to the relay module
2. Upload the ESP32 code
3. Connect ESP32 and the system to the same WiFi network
4. Start the Flask server

---

# System Outputs

## Home Interface
- Live monitoring dashboard
- Mode selection panel

## Zone Detection
- Real-time person detection
- Bounding box visualization

## Auto Mode
- Automatic fan activation
- Zone-wise occupancy detection

## Manual Mode
- Manual fan ON/OFF controls
- User override functionality

---

# Demo

Project demonstration video:

```bash
demo/final Classroom demo.mp4
```

---

# Applications

- Smart classrooms
- Smart offices
- Energy-efficient buildings
- Home automation systems
- Occupancy-based cooling systems

---

# Future Enhancements

- Mobile application integration
- Voice assistant support
- Adaptive fan speed control
- Cloud-based monitoring
- Energy analytics dashboard
- Multi-camera support
- IoT dashboard integration

---

# Advantages

- Reduces electricity wastage
- Improves automation efficiency
- Enables intelligent occupancy detection
- Cost-effective smart solution
- Real-time monitoring and control

---

# Authors

Developed as part of the B.Tech Project in Artificial Intelligence and Data Science.

Adi Shankara Institute of Engineering and Technology, Kalady

---

# License

This project is developed for academic and research purposes.

---

# Acknowledgement

We sincerely thank our faculty members, project guides, and institution for their continuous support and guidance throughout the development of this project.

---

# Conclusion

The Smart Motion and Zone-Based Fan Control System demonstrates the integration of Artificial Intelligence, Computer Vision, and IoT technologies for intelligent environmental automation.

By combining YOLOv8-based human detection with ESP32-controlled fan automation, the system provides an energy-efficient and scalable smart control solution suitable for modern smart environments.

---

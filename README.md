🌬️ Smart Motion and Zone-Based Fan Control System Using YOLOv8 

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![Flask](https://img.shields.io/badge/Flask-Backend-lightgrey)  
![YOLOv8](https://img.shields.io/badge/YOLOv8-Object%20Detection-green)  
![ESP32](https://img.shields.io/badge/Hardware-ESP32-orange)  


📖 Overview  
This project presents a **Smart Motion and Zone-Based Fan Control System** that uses **YOLOv8** for real-time human detection and automatically controls fans in different room zones.  

The system is designed to save energy and improve comfort by:  
- Detecting people in zones (via camera + YOLO).  
- Turning **fans ON/OFF automatically**.  
- Providing a **web interface** for live monitoring & manual control.  


🚀 Features  
- Real-time human detection with **YOLOv8**  
- Zone-based control (supports 4 zones)  
- Auto Mode – fans switch automatically  
- Manual Mode – manual override via UI  
- Live video feed with bounding boxes  
- Energy-efficient (turns OFF after 5 sec inactivity)  


📂 Project Structure  
├── demo/ # Reports & demo videos
├── docs/ # Documentation
├── templates/ # HTML templates
├── app.py # Flask app
├── backend.py # YOLO + fan control logic
├── frontend.html # Web UI
├── ESP32_Code/ # Microcontroller code
└── README.md # Project description


---

⚙️ Requirements  
- Python 3.8+  
- Flask  
- OpenCV  
- Ultralytics YOLOv8  
- ESP32/Arduino with relay module  

Install dependencies:  
pip install flask opencv-python ultralytics requests

Run the backend:

python backend.py


Open in browser:

http://127.0.0.1:5000/


Connect ESP32 to same WiFi & upload the Arduino code.

📸 Screenshots

🔹 Home Page


🔹 Zone Detection


🔹 Fan Control (Auto Mode)


🔹 Fan Control (Manual Mode)


🎥 Demo Video  
📌 [Click here to watch the demo](demo/final%20Classroom%20demo.mp4)  

🔮 Future Enhancements

Mobile app with notifications

Voice Assistant (Alexa/Google) integration

Adaptive fan speed based on no. of people

Energy usage reports

👩‍💻 Team Members 

Malavika V R 

Merin Philip 

Nandana E S 

Christina Dixon

Guide: Asst. Prof. Sabitha M G

📜 License
This project is part of B.Tech CSE(AI) Mini Project at
Adi Shankara Institute of Engineering and Technology, Kalady.

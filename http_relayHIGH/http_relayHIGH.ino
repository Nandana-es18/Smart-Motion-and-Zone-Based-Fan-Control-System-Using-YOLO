#include <WiFi.h>
#include <WebServer.h>  // Web server library

const char* ssid = "Rajesh babu";       // Your Wi-Fi SSID
const char* password = "43211234";  // Your Wi-Fi password

WebServer server(80);  // Initialize web server on port 80

// Define GPIO pins for the relay module (Adjust based on wiring)
const int relayPins[4] = {26, 27, 32, 33};

// Function to handle zone control
void handleZoneControl() {
    if (server.hasArg("zone") && server.hasArg("status")) {
        int zone = server.arg("zone").toInt();
        int status = server.arg("status").toInt();
        
        if (zone >= 1 && zone <= 4) {
            digitalWrite(relayPins[zone - 1], status ? LOW : HIGH);  // Active LOW logic
            server.send(200, "text/plain", "Zone " + String(zone) + " set to " + (status ? "ON" : "OFF"));
            Serial.println("Zone " + String(zone) + " set to " + (status ? "ON" : "OFF"));
        } else {
            server.send(400, "text/plain", "Invalid Zone");
        }
    } else {
        server.send(400, "text/plain", "Missing Parameters");
    }
}

void setup() {
    Serial.begin(115200);
    
    // Connect to Wi-Fi
    WiFi.begin(ssid, password);
    Serial.print("Connecting to Wi-Fi");

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println("\nWiFi connected!");
    Serial.print("ESP32 IP Address: ");
    Serial.println(WiFi.localIP());

    // Set relay pins as OUTPUT and turn them OFF initially (HIGH for active LOW logic)
    for (int i = 0; i < 4; i++) {
        pinMode(relayPins[i], OUTPUT);
        digitalWrite(relayPins[i], HIGH);  // Ensure all relays are OFF initially
    }

    // Define the homepage route
    server.on("/", []() {
        server.send(200, "text/html", "<h1>ESP32 Web Server is Running!</h1>");
    });

    // Define the route for zone control
    server.on("/control", HTTP_GET, handleZoneControl);

    server.begin();
    Serial.println("HTTP server started");
}

void loop() {
    server.handleClient();
} 

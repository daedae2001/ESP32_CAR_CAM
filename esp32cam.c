#include <WiFi.h>
#include <Wire.h>
#include <SPI.h>
#include <esp_camera.h>

const char *ssid = "your_network_SSID";
const char *password = "your_network_password";

WiFiServer server(80);

void setup() {
  Serial.begin(115200);
  // Inicializa la cámara
  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = 5;
  config.pin_d1 = 18;
  config.pin_d2 = 19;
  config.pin_d3 = 21;
  config.pin_d4 = 36;
  config.pin_d5 = 39;
  config.pin_d6 = 34;
  config.pin_d7 = 35;
  config.pin_xclk = 0;
  config.pin_pclk = 22;
  config.pin_vsync = 25;
  config.pin_href = 23;
  config.pin_sscb_sda = 26;
  config.pin_sscb_scl = 27;
  config.pin_pwdn = 32;
  config.pin_reset = -1;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG;
  // configura la resolución de la cámara
  config.frame_size = FRAMESIZE_QVGA;
  // Inicializa la cámara
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.println("Camera init failed with error 0x%x", err);
    return;
  }

  // Inicializa WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Inicializa el servidor web
  server.begin();
  Serial.println("Server started");
}

void loop() {
  // Acepta una conexión cliente
  WiFiClient client = server.available();
  if (!client) {
    return;
  }
  while (!client.available()) {
    delay(1);
  }

  // Lee la petición del cliente
  String request = client.readStringUntil('\r');
  Serial.println("Client request: " + request);
  client.flush();

  // Envía la imagen capturada por la cámara al cliente
  String response = "HTTP/1.1 200 OK\r\n";
  response += "Content-Type: image/jpeg\r\n\r\n";

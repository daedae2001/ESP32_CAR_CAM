#include <WiFi.h>
#include <esp_camera.h>
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include <ESP32_Servo.h>

const char *ssid = "your_ssid";
const char *password = "your_password";

Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *leftMotor = AFMS.getMotor(1);
Adafruit_DCMotor *rightMotor = AFMS.getMotor(2);

void setup()
{
    Serial.begin(115200);

    // Conecta a la red WiFi
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(1000);
        Serial.println("Conectando a WiFi...");
    }
    Serial.println("Conectado a WiFi");

    AFMS.begin();
    leftMotor->setSpeed(200);
    rightMotor->setSpeed(200);

    // Inicia el servidor web
    httpd_config_t config = HTTPD_DEFAULT_CONFIG();
    httpd_uri_t index_uri = {
        .uri = "/",
        .method = HTTP_GET,
        .handler = index_handler,
        .user_ctx = NULL};
    httpd_handle_t server = NULL;
    if (httpd_start(&server, &config) == ESP_OK)
    {
        httpd_register_uri_handler(server, &index_uri);
    }
}

void loop()
{
    // Mueve el carro hacia adelante
    leftMotor->run(FORWARD);
    rightMotor->run(FORWARD);
    delay(1000);

    // Detiene el carro
    leftMotor->run(RELEASE);
    rightMotor->run(RELEASE);
    delay(1000);

    // Mueve el carro hacia atrás
    leftMotor->run(BACKWARD);
    rightMotor->run(BACKWARD);
    delay(1000);

    // Detiene el carro
    leftMotor->run(RELEASE);
    rightMotor->run(RELEASE);
    delay(1000);
}

esp_err_t index_handler(httpd_req_t *req)
{
    camera_fb_t *fb = NULL;
    esp_err_t res = ESP_OK;
    fb = esp_camera_fb_get();
    if (!fb)
    {
        Serial.println("Camera capture failed");
        httpd_resp_send_500(req);
        return ESP_FAIL;
    }

    httpd_resp_set_type(req, "image/jpeg");
    httpd_resp_set_hdr(req, "Content-Disposition", "inline; filename=capture.jpg");
    httpd_resp_set_hdr(req, "Access-Control-Allow-Origin", "*");

    size_t fb_len = 0;
    if (fb->format == PIXFORMAT_JPEG)
    {
        fb->len;
        res = httpd_resp_send(req, (const char *)fb->buf, fb->len);
    }
    else
    {
        jpeg_chunking_t jchunk = {
            .len = fb->len,
            .buf = fb->buf,
            .offset = 0};
        res = httpd_resp_send_chunk(req, (const char *)jchunk.buf, jchunk.len);
        while (res == ESP_OK)
        {
            fb = esp_camera_fb_get();
            if (!fb)
            {
                Serial.println("Camera capture failed");
                httpd_resp_send_500(req);
                return ESP_FAIL;
            }
            jchunk.buf = fb->buf;
            jchunk.len = fb->len;
            jchunk.offset += jchunk.len;
            res = httpd_resp_send_chunk(req, (const char *)jchunk.buf, jchunk.len);
            esp_camera_fb_return(fb);
        }
    }
    esp_camera_fb_return(fb);
    return res;
}
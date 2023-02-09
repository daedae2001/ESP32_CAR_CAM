import requests

url = "http://<esp32-cam-ip>/capture"

response = requests.get(url)

if response.status_code == 200:
    with open("captured_image.jpg", "wb")

import cv2
import numpy as np

# Cargar el modelo de detección de rostros
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Cargar el modelo de reconocimiento de rostros
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read("modelo_entrenado.yml")

# Función para predecir la identidad de la persona
def predict_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        id_, conf = face_recognizer.predict(roi_gray)
        if conf >= 45: # Confianza mínima para una identificación
            return id_
    return None

# Cargar la imagen
img = cv2.imread("imagen_persona.jpg")

# Realizar la predicción
prediction = predict_face(img)
if prediction is not None:
    print("La persona es:", prediction)
else:
    print("No se pudo identificar a la persona.")


"""
Este código asume que tienes previamente entrenado un modelo de reconocimiento de rostros y guardado en un archivo modelo_entrenado.yml.

También debes tener el archivo haarcascade_frontalface_default.xml en la misma carpeta que tu script, que es el modelo de detección de rostros de OpenCV.

"""


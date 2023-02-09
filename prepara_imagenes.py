import cv2
import os

# Carga del clasificador de caras Haar
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Ruta al directorio con imágenes
directory = 'ruta/a/directorio/con/imágenes'

# Recorre todas las imágenes en el directorio
for filename in os.listdir(directory):
    # Carga de la imagen
    img = cv2.imread(os.path.join(directory, filename))
    # Convertir a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detectar caras
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # Recortar y guardar cada cara detectada
    for (x, y, w, h) in faces:
        face = img[y:y+h, x:x+w]
        face = cv2.resize(face, (150, 150))
        cv2.imwrite('ruta/para/guardar/imágenes/recortadas/' + filename, face)

    """
    Este código recorre un directorio y carga cada imagen. Luego, utiliza la función cv2.CascadeClassifier para cargar el clasificador de caras Haar y detectar caras en la imagen. Por último, recorta cada cara detectada y la guarda en un nuevo directorio.

Nota: Debes tener instalado OpenCV y descargar el archivo haarcascade_frontalface_default.xml para poder ejecutar este código correctamente.
    https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
    """